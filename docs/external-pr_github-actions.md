# External PRs with Github Actions

## The Problem

A common problem in open source projects, is needing to run privileged
CI jobs (access to secrets, write access) against PRs from untrusted forks.

For example, a job might need to execute new unit tests from a fork (untrusted),
and then upload code coverage results to a service using a secret API key (trusted).

If a Github Actions workflow runs untrusted code (forked repo) in a trusted
context (secrets/write), secrets can be stolen and the repo written to. Tests
are the most obvious avenue for untrusted execution, but there are many
possibilities.

Several solutions to the problem exist, with different tradeoffs.

## Github Action Triggers and Permissions

There are a few events that can help with running the trusted and
untrusted parts of the pipeline, depending on your needs.

|                | `pull_request` | `pull_request_trigger` | `workflow_run`   |
|----------------|----------------|------------------------|------------------|
| Triggered by   | Pull request   | Pull request           | Another workflow |
| Secrets access | No             | Yes                    | Yes
| Write access   | No             | Yes                    | Yes
| Runs from      | Forked repo    | Base repo              | Base repo



## Solutions

### 1: pull_request

Use the standard unprivileged `pull_request` trigger, which runs in the
context of the forked repo.

Example:

```
on:
	pull_request: {}

jobs:

	# Run forked repo PR in forked repo context, unprivileged
	test:
    runs-on: ubuntu-latest
    steps:

			# Checkout the forked PR code by default
      - name: Checkout
			  uses: actions/checkout@v2

			# Fails without access to secrets
      - name: Privileged processing
        run: echo "Some sensitive command that executes code (tests) and/or uses secrets"
```

Flow:
1. Forked repo opens a PR.
1. The `pull_request` event triggers the workflow.
1. The workflow runs in the unprivileged context of the forked repo's PR.
1. The workflow checks out the PR branch by default.
1. Workflow jobs that need access to secrets run, and fail.
1. The maintainer reviews the PR.
1. To merge, the maintainer has to override the failing checks.

Tradeoffs:
- Pro: simple, secure.
- Con: privileged workflows won't work for PRs from forked repositories.

Use this solution if you can remove jobs that need privileged access, or
you are alright with those jobs never passing for PRs from forks.


### 2: pull_request_target + fork checkout (insecure)

Use the newer privileged `pull_request_target` trigger, which runs in the
context of your original repo and has secrets/write access.

Since it runs in the context of the source repo, the new PR
code needs to be checked out from the forked repo.

Example:

```
on:
  pull_request_target: {}

jobs:

	# Run forked repo PR in base repo context, automatically
	test:
    runs-on: ubuntu-latest
    steps:

			# Checkout the forked repo PR code into the base repo
      - name: Checkout
			  uses: actions/checkout@v2
				with:
					ref: ${{ github.event.pull_request.head.sha }}

			# Passes, with forked PR code analyzed in privileged context
      - name: Privileged processing
        run: echo "Some sensitive command that executes code (tests) and/or uses secrets"
```

Flow:
1. Forked repo opens a PR.
1. The `pull_request_target` event triggers the workflow.
1. The workflow runs in the privileged context of the base repo.
1. The workflow is explicitly instructed to check out the forked PR branch.
1. Workflow jobs that need access to secrets run against the remote branch,
    and pass.
1. If jobs execute the untrusted PR code in the trusted context, secrets
    can be leaked, and the base repo can be written to, before anyone reviews.
1. The maintainer reviews the PR.
1. The PR can be merged.

This introduces a security issue, where untrusted code (fork repo)
runs in a trusted context (base repo). A malicious PR against
an insecure configuration can steal secrets or write to the repo.
A manual review doesn't happen until _after_ running the PR in the pipeline.

Tradeoffs:
- Pro: simple, privileged workflows work for PRs from forked repositories.
- Con: vulnerable to unauthorized secrets and write access from malicious PRs.

Use this solution if the workflow jobs have no chance of running
untrusted code from fork PRs.
From [Github's Security Lab](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/)
on `pull_request_target`:

> The intent is to use the trigger for PRs that do not require dangerous
> processing, say building or running the content of the PR.


### 3: pull_request_target + label condition + fork checkout

Use the privileged `pull_request_target` trigger, but gated behind a label
that only the base repository maintainer can modify.

This idea comes from
[Github Security Lab's](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/)
advice on remediating the issue in solution #2.

> Add a condition to the pull_request_target to run only if a certain label is
> assigned the PR, like `safe to test` that indicates the PR has been vetted by
> someone with write privileges to the target repository:

Example:

```
on:
	pull_request_target:
		types: [labeled]

jobs:

	# Run forked repo PR in base repo context, but only if labelled
	test:
    runs-on: ubuntu-latest
		if: contains(github.event.pull_request.labels.*.name, 'safe to test')
    steps:

			# Checkout the forked repo PR code into the base repo
      - name: Checkout
			  uses: actions/checkout@v2
				with:
					ref: ${{ github.event.pull_request.head.sha }}

			# Passes, with forked PR code analyzed in privileged context, after review
      - name: Privileged processing
        run: echo "Some sensitive command that executes code (tests) and/or uses secrets"
```

Flow:
1. Forked repo opens a PR.
1. The maintainer reviews the PR.
1. The maintainer applies a label (i.e. `safe`) to the forked PR.
1. The `pull_request_target` event of type `labeled` triggers the workflow.
1. The workflow runs in the privileged context of the base repo.
1. The workflow is explicitly instructed to check out the forked PR branch.
1. Workflow jobs that need access to secrets run against the remote branch,
    and pass.
1. The PR can be merged.

The risk of forked code stealing secrets is managed by allowing maintainers
to review the PR _before_ running in the pipeline.

Tradeoffs:
- Pro: approval before pipeline execution, works with forked repositories.
- Con: requires labeling each PR, in addition to approval. Have to remove
		and reapply the label each time (can be configured not to). If configured
		to automatically run once the label is applied, submitter can commit
    malicious code after receiving the label.


### 4: pull_request_target + maintainer approvals + fork checkout

Use the privileged `pull_request_target` trigger, but gated behind an
environment protection rule that enforces a manual maintainer approval.

This comes from the post
[Using Environment Protection Rules to Secure Secrets When Building External Forks with pull_request_target](https://dev.to/petrsvihlik/using-environment-protection-rules-to-secure-secrets-when-building-external-forks-with-pullrequesttarget-hci)

> The advantage of this approach is that you can assign a group of reviewers
> who'll receive an email notification about the pending workflow and can review
> and approve it in a single click.

Example:

1. Configure a new repo environment.
1. Add people as assigned reviewers, allowed to approve PRs.
1. Apply the environment rule to all branches.
1. Add secrets for the workflow to use.

```
on: [pull_request_target]

jobs:

	# Deliberately fails and will not continue, until PR is approved.
  approve:
    runs-on: ubuntu-latest
    steps:

    - name: Approve
      run: echo "Pull requests require approval before running further actions."

	# Run forked repo PR in base repo context, once approval passes
	test:
    runs-on: ubuntu-latest
    steps:

			# Checkout the forked repo PR code into the base repo
      - name: Checkout
			  uses: actions/checkout@v2
				with:
					ref: ${{ github.event.pull_request.head.sha }}

			# Passes, with forked PR code analyzed in privileged context, after review
      - name: Privileged processing
        run: echo "Some sensitive command that executes code (tests) and/or uses secrets"

      # Show configured environment level secret value
      - name: Env Secret
        run: echo "ENV_SECRET_VALUE = ${{ secrets.ENV_LEVEL_SECRET }}"
```

Flow:
1. Forked repo opens a PR.
1. The maintainer reviews the PR.
1. The maintainer applies a label (i.e. `safe to test`) to the forked PR.
1. The `pull_request_target` event of type `labeled` triggers the workflow.
1. The workflow runs in the privileged context of the base repo.
1. The workflow is explicitly instructed to check out the forked PR branch.
1. Workflow jobs that need access to secrets run against the remote branch,
    and pass.
1. The PR can be merged.

Tradeoffs:
- Pro: approval before pipeline execution, single step approval, works
    with forked repositories, secrets are per environment instead of per repo.
- Con: additional setup for environmental protection rule configuration. Feels
    a little clunky, meant for CD rather than CI. Uses "deployment approval"
    (separate from PR review approval), and does not show up on the PR. Message
    on the PR shows "user deployed to PR Approval 10 minutes ago," but it isn't
    a deployment.


### 5: pull_request + workflow_run

This solution splits the workflow into two parts:
- An unprivileged workflow using `pull_request`, triggered by the forked PR.
- A privileged workflow using `workflow_run`, triggered by the first workflow.

Data is passed from the unprivileged workflow to the privileged one
by uploading and downloading files, using the `actions/upload-artifact`
and `actions/github-script` actions.

The potentially dangerous code (like tests) are executed in the unprivileged context
of the forked repo, and data is handed off to a privileged context for uploading to
services. How can code coverage checks be enforced in that case?

Example:

```
```

A significant drawback to this approach is that checks executed in the second
`workflow_run` workflow can't be enforced in the forked PR. They don't even
show up in actions.


Flow:
1. Forked repo opens a PR.


Tradeoffs:
- Pro:
- Con: additional complexity, checks in the privileged workflow aren't
    enforced in the forked PR.


## Resources

https://securitylab.github.com/research/github-actions-preventing-pwn-requests/

> TL;DR: Combining pull_request_target workflow trigger with an explicit checkout
> of an untrusted PR is a dangerous practice that may lead to repository
> compromise.

> The reason to introduce the pull_request_target trigger was to enable workflows
> to label PRs (e.g. needs review) or to comment on the PR. The intent is to use
> the trigger for PRs that do not require dangerous processing, say building or
> running the content of the PR.


https://dev.to/petrsvihlik/using-environment-protection-rules-to-secure-secrets-when-building-external-forks-with-pullrequesttarget-hci


https://github.com/codeclimate/test-reporter/issues/452

> My repo has diff-coverage running on any PR. This has been working great for
> PRs made within my own repo, but we found today that it doesn't work on a
> PR from a forked PR.
