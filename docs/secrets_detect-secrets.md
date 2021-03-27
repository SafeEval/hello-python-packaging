# Secrets: detect-secrets

https://github.com/Yelp/detect-secrets

Python package from Yelp to detect secrets in code repos, and prevent them from
being committed.

Includes a pre-commit hook.

Records discovered secrets as hashes in a config file that lives in the repo,
allowing developers to quantify and chip away at historical debt.

## Usage

### Initial Baseline

1. Install the package: `pip install detect-secrets`
2. Create baseline of repo secrets: `detect-secrets scan > .secrets.baseline`
3. Audit the baseline, to review and make decisions about each secret:
    `detect-secrets audit .secrets.baseline`
4. Commit the new baseline file to the repo.

A powerful aspect of `detect-secrets` is that secrets can be flagged in the
initial baseline, without remediation. This allows developers to get a quick
baseline, separate of remediation, instead of having to do everything up front.


### Ongoing

1. Update the baseline periodically: `detect-secrets scan --baseline .secrets.baseline`
2. Audit the baseline, to review and make decisions about each secret:
    `detect-secrets audit .secrets.baseline`
3. Commit the updated baseline file to the repo.

## Pre-Commit Hook

The repo includes a pre-commit hook.

```
# .pre-commit-config.yaml
repos:
-   repo: https://github.com/Yelp/detect-secrets
    rev: v1.0.3
    hooks:
    -   id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
        exclude: package.lock.json
```

Any new secret will be detected on commit. The developer will be notified,
with some remediation guidance.

If the secret is a false positive, the developer:
1. Updates the baseline
2. Audits the baseline, marking the new "secret" as a false positive.
3. Commits the new baseline, which will be included in the PR.
