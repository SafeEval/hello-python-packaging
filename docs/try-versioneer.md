# Versioning with Versioneer

For Python package versioning, use the 
[`versioneer` package](https://github.com/python-versioneer/python-versioneer).
It will automatically bump your package version, based on Git tags and commit
status.

Limitations:
- Only works with `setup.py`, 
  not `setup.cfg` ([#245](https://github.com/python-versioneer/python-versioneer/issues/245))
  or `pyproject.toml` ([#146](https://github.com/python-versioneer/python-versioneer/issues/146)).

Steps:
1. Add block to `setup.cfg`.
2. Install `versioneer` package.
3. Install the versioneer modules.

The `setup.cfg` block ([parameter docs](https://github.com/python-versioneer/python-versioneer/blob/master/INSTALL.md#installation)):

```
[versioneer]
VCS = git
style = pep440
versionfile_source = hello_pypi/_version.py
versionfile_build = None
tag_prefix = 'hello-pypi-'
parentdir_prefix = 'hello-pypi-'
```

Install the versioneer package.

```
pip install versioneer
```

Install the versioneer modules.

```
versioneer install
```

