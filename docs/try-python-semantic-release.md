# Python Semantic Release


## Resources

- [hello-pypi (Test PyPI)](https://test.pypi.org/project/js-hello-pypi/)
- [Docs: Getting Started](https://python-semantic-release.readthedocs.io/en/latest/#getting-started)
- [Docs: Commands](https://python-semantic-release.readthedocs.io/en/latest/#commands)
- [Docs: Env Vars](https://python-semantic-release.readthedocs.io/en/latest/envvars.html)
- [Github](https://github.com/relekang/python-semantic-release)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)
- [Angular Commit](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits)
- [Commit examples](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.8sw072iehlhg)

## Setup

Install Python Semantic Release

```
python3 -m pip install python-semantic-release
```

Create a `hello_pypi/__version__.py` file.

```
__version__ = "0.0.1"
```

Create a lightweight `setup.py` file. This will allow builds to work.

```
from setuptools import setup
from hello_pypi.__version__ import __version__

setup(version=__version__)
```

Add lines to `setup.cfg`, configuring it for build and release.

```
[semantic_release]
# The SCM to use.
hvcs = github

# The primary branch to commit against.
branch = try-python-semantic-release

# Where to read/write version information.
version_variable = hello_pypi/__version__.py:__version__

# Does `publish` subcommand release to PyPI?
#upload_to_pypi = false

# Should `publish` subcommand use the test PyPI index?
repository = testpypi

# Does `publish` subcommand upload to Github Release?
upload_to_release = false
```

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


## Commits and Versions

PSR looks for commit messages that follow the
[Angular style](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits)
of commit messages, to automatically determine the next version.

If a commit message does not match the angular style, it is ignored.

Commit messages can look like:

> feat: Added my cool new feature

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
`chore:`    |       | Changes to the build process or auxiliary tools and libraries such as documentation generation

### Breaking Changes

To commit a breaking change (major version bump), the commit message header
needs to be one of the above keywords, and have the body or footer
start with `BREAKING CHANGE: `, followed by the message.

```
feat(big-thing): Program now does big thing

BREAKING CHANGE: the big feature messes everything up
```


## Generating and Updating the Changelog

The `publish` subcommand will create or update a changelog file, and
commit it to the repo in the release commit (the one that gets tagged).

The `version` subcommand does not generate a changelog.

The `changelog` subcommand only shows the changes from the last
published version.


## Viewing Current and Next Commit

View current version. Can be used in scripts.

```
semantic-release print-version --current
```

View the upcoming version. Can be used in scripts.


## Cutting a New Version

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



## Full Manual Flow

Last tagged version was `0.2.0`.

Show current version.

```
$ semantic-release print-version --current
0.2.0

$ cat hello_pypi/__version__.py
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
warning: Changelog file not found: /home/ubuntu/Documents/git/hello-pypi/CHANGELOG.md - creating it.
Bumping with a patch version to 0.2.2
Pushing new version
```






