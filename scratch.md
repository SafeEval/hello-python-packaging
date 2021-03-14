# Scratch

Scratch pad for testing versioning and commit messages.

> feat: something cool
```
$ semantic-release version
Creating new version
Current version: 0.0.2
Bumping with a minor version to 0.1.0
$ git tag --list
v0.1.0
$ cat hello_pypi/__version__.py
__version__ = "0.1.0"
```

> feature: more cool stuff
```
$ semantic-release version
Creating new version
Current version: 0.1.0
No release will be made.
```

> feat: something cool again
```
$ semantic-release version
Creating new version
Current version: 0.1.0
Bumping with a minor version to 0.2.0
```

Generated a changelog.

```
$ semantic-release changelog
### Feature
* Something cool again ([`3bede4a`](https://github.com/SafeEval/hello-pypi/commit/3bede4a25d0a69c3c86ef1bbb76fd35566579225))
```

> fix(foo): Fixed the foo bug

```
$ semantic-release print-version --current
0.2.0
$ semantic-release print-version
0.2.1
```

> fix(foo): Fixed the second foo bug

```
$ semantic-release publish
warning: Changelog file not found: /home/ubuntu/Documents/git/hello-pypi/CHANGELOG.md - creating it.
Bumping with a patch version to 0.2.2
Pushing new version
```

> fix(foo): Fixed the third foo bug
Committed
> fix(foo): Fixed the fourth foo bug
Committed

Created new version (`version`).
- Changelog was not updated. The `changelog` subcommand only shows most recent changes.
- Cannot then publish a change. The `version` and `publish` subcommands are mutually exclusive.

> fix(foo): Fixed the fifth foo bug
Committed

Published new version (`publish`).
- Changelog skipped over the changes created by `version`. Only includes `publish` changes.
- Included `0.2.2`, skipped `0.2.3`, included `0.2.4`.

> feat(bar): new bar feature
Committed

> fix(bar): new bar feature
Committed

The next version is bumped by a major point, from the feature.

```
$ semantic-release print-version
0.3.0
```

> break: breaking change 1
Committed. Still thinks `0.3.0`.

> This is a mess. Destroys everything!
>
> BREAKING CHANGE: Disaster. FOOBAR!
Committed. Still thinks `0.3.0`.

> BREAKING CHANGE: Disaster. FOOBAR! 2
Committed. Still thinks `0.3.0`.

> This is a mess. Destroys everything!
>
> Some body content here.
>
> BREAKING CHANGE: Disaster. FOOBAR!
Committed. Still thinks `0.3.0`.


> feat(bigthing): Added some big feature
>
> BREAKING CHANGE: the big feature messes everything up
Committed, this works!!! `1.0.0`.


The default build process requires `setup.py` to work.

Added the `PYPI_TOKEN` and `GH_TOKEN`.

Published, and it committed the changelog to Github and released to PyPI.


Checking out a new branch, adding some commits,
and opening a PR against the PSR test branch.


More testing

