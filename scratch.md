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




