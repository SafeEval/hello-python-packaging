# Versioning with Python Semantic Release

To setup a new project, look at:
- [File Setup](#file-setup)
- [Environment Setup](#environment-setup)
- [Automatic Releases](#automatic-releases)

For information on how to write commit messages,
look at [Commits and Versions](#commits-and-versions)


## Setup

### File Setup

This is required for both manual and Github Actions environments.

Create a `hello_pp/__version__.py` file.

```
__version__ = "0.0.1"
```

Create a lightweight `setup.py` file. This will allow builds to work.

```
from setuptools import setup
from hello_pp.__version__ import __version__

setup(version=__version__)
```

Add lines to `setup.cfg`, configuring it for build and release.

```
[semantic_release]
# The SCM to use.
hvcs = github

# The primary branch to commit against.
branch = main

# Where to read/write version information.
version_variable = hello_pp/__version__.py:__version__

# Does `publish` subcommand release to PyPI?
upload_to_pypi = true

# Should `publish` subcommand use the test PyPI index?
repository = testpypi

# Does `publish` subcommand upload to Github Release?
upload_to_release = true
```

### Environment Setup

This is required for both manual and Github Actions environments.

Add the PyPI token to a PSR specific environment variable, that
allows the `publish` subcommand to upload a new release to PyPI.

```
export PYPI_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Add the Github token with `repo` scope to a PSR specific environment variable,
that allows the `publish` subcommand to push commits.
([Github configuration](https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/index.html#automatic-github))

```
export GH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxx
```

### Automatic Release with Github Actions (Official)

There is an official [Github Action](https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/github-actions.html)
for running `semantic-release publish`.

Configure the `PYPI_TOKEN` and `GH_TOKEN` values in the Github repo's secrets,
similarly to the local environment setup above.

The workflow below specifies a manual release process, while the commented out
block would release on every PR merged into `main`.

```
# .github/workflows/semantic-release.yaml

name: Semantic Release

# Automatic releases.
# on:
#   push:
#     branches:
#       - main

# Manual releases.
on: workflow_dispatch

jobs:
  release:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
      with:
        persist-credentials: false
        fetch-depth: 0

    - name: Python Semantic Release
      uses: relekang/python-semantic-release@master
      with:
        pypi_token: ${{ secrets.PYPI_TOKEN }}
        github_token: ${{ secrets.GH_TOKEN }}
```

This works even when branch protection is set on `main`, because a personal
access token allows Semantic Release to commit the new changelog and release
to the `main` branch.

This is outlined in the documentation
([source](https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/github-actions.html?highlight=protection)):

> Warning
>
> The GITHUB_TOKEN secret is automatically configured by GitHub, with the same
> permissions as the user who triggered the workflow run. This causes a problem
> if your default branch is protected.
>
> You can work around this by storing an administrator’s Personal Access Token as
> a separate secret and using that instead of GITHUB_TOKEN. In this case, you
> will also need to pass the new token to actions/checkout (as the token input)
> in order to gain push access.


### Executable Setup

his isn't needed, unless releasing from local machine, or using custom
Github Action.  Install Python Semantic Release

```
python3 -m pip install python-semantic-release
```


## Commits and Versions

Python Semantic Release looks for commit messages that follow the
[Angular style](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits)
of [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#summary)
commit messages, to automatically determine the next version.

If a commit message does not match the format, it is ignored.

Generic commit messages can look like:

> feat: Added my cool new feature

Topic/area specific commit messages can look like:

> feat(auth): Some new auth feature

### Patch Bump: Fixes

When fixing a bug, a a commit could look like:

> fix: Fixed some bug.

To be specific about the category of fix:

> fix(some-feature): Fixed some bug in some feature.


### Minor Bump: Features

When adding a feature, a commit could look like:

> feat: Added my cool new feature

To be specific about the category of feature:

> feat(auth): Some new auth feature


### Major Bump: Breaking Changes

To commit a breaking change (major version bump), the commit message header
needs to be one of the below keywords, and have the body or footer
start with `BREAKING CHANGE: `, followed by the message.

```
feat(big-thing): Program now does big thing

BREAKING CHANGE: the big feature messes everything up
```

### Standard Keywords

Available keywords are:

Prefix      | Bump  | Purpose
------------|-------|------------------
`fix:`      | Patch | Bug fix
`feat:`     | Minor | New feature
`docs:`     |       | Documentation change
`style:`    |       | Non-functional formatting code change
`refactor:` |       | Non-functional code change
`perf:`     |       | Performance code change
`test:`     |       | Test code changes
`chore:`    |       | Non-app changes to build/tooling/infra


## Manual Releases

### Explicit Manual Version Bumps

Show the next `--patch`, `--minor`, or `--major` version number.

```
semantic-release print-version --patch
```

Actually bump to the next version. Changelog won't be affected,
unless there are any new Conventional Commits to include.
A new PyPI release will be attempted, but not succeed unless
crednetials are configured.

```
$ semantic-release publish --patch
Bumping with a patch version to 4.0.4
Pushing new version
Building distributions
...
removing build/bdist.linux-x86_64/wheel
Uploading to PyPI
error: Missing credentials for uploading to PyPI
```

A new Git tag will be created for the version.

```
$ git tag
...
v4.0.4
```


### Generate and Update Changelog

The `publish` subcommand will create or update a changelog file, and
commit it to the repo in the release commit (the one that gets tagged).

The `version` subcommand does not generate a changelog.

The `changelog` subcommand only shows the changes from the last
published version.


### Viewing Current and Next Commit

View current version. Can be used in scripts.

```
semantic-release print-version --current
```

View the upcoming version. Can be used in scripts.



### Creating a New Release

To create a new version:

```
semantic-release version
```

This will:
- Identify the current version, from `__version__.py` and/or Git tag.
- Scan commit messages since that version for keywords.
- Calculate the new version.
- Update `__version__.py` with the new version.
- Commit the updated version file, and tag it with the new version.

This will not:
- Generate a new changelog.


### Full Manual Flow

Last tagged version was `0.2.0`.

Show current version.

```
$ semantic-release print-version --current
0.2.0

$ cat hello_pp/__version__.py
__version__ = "0.2.0"
```

Make one or more commits, using Conventional Commit messages.

```
$ git commit -am "fix(foobar): Fixed the foobar bug"
```

Check current and next versions.

```
$ semantic-release print-version --current
0.2.0
$ semantic-release print-version
0.2.1
```

Only shows the changes from most recent release.

```
semantic-release changelog
```

Dry run of bumping to version, to verify what it'll do.

```
$ semantic-release version --noop
Creating new version
Current version: 0.2.0
warning: No operation mode. Should have bumped from 0.2.0 to 0.2.1
```

Cut a new version (updates the version file, commits it, tags).

```
$ semantic-release version
Creating new version
Current version: 0.2.0
Bumping with a patch version to 0.2.1
```

Cut a new version (generates changelog, updates the version file, commits it, tags).
This will generate a changelog if none exist.

```
$ semantic-release publish
warning: Changelog file not found: /home/ubuntu/Documents/git/hello-python-project/CHANGELOG.md - creating it.
Bumping with a patch version to 0.2.2
Pushing new version
```

If the `PYPI_TOKEN` and `GH_TOKEN` values are set, the new package will be released to Github and PyPI.


## Resources

- [hello-python-project (Test PyPI)](https://test.pypi.org/project/hello-python-project/)
- [Docs: Getting Started](https://python-semantic-release.readthedocs.io/en/latest/#getting-started)
- [Docs: Commands](https://python-semantic-release.readthedocs.io/en/latest/#commands)
- [Docs: Env Vars](https://python-semantic-release.readthedocs.io/en/latest/envvars.html)
- [Docs: Github Actions](https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/github-actions.html)
- [Github](https://github.com/relekang/python-semantic-release)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)
- [Angular Commit](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits)
- [Commit examples](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.8sw072iehlhg)
