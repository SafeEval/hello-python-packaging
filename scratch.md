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




