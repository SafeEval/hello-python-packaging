# Versioning with Python Build Reasonableness

Tool from OpenStack.
- Versioning
- Change logs
- Release notes

Key points:
- Must use a `setup.py`, but it is minimal.
- Looks for keywords in the commit, like "bugfix" and "feature"

## Resources

https://docs.openstack.org/pbr/latest/

https://docs.openstack.org/pbr/latest/user/features.html#version

https://julien.danjou.info/packaging-python-with-pbr/

https://tech.xlab.si/blog/creating-python-packages-using-pbr/

https://stackoverflow.com/questions/48383737/get-version-from-git-tags-through-pbr

https://stackoverflow.com/questions/55921981/how-can-i-use-pbr-version-from-source

## Setup

Install `pbr`

```
pip install pbr
```


Write `setup.py`

```
from setuptools import setup

setup(setup_requires=["pbr"], pbr=True)
```

## Versions

PBR looks at Git commit history, for the most recent version tag,
and adds "dev" versions on top of it until another tag is set.

> If the currently checked out revision is tagged, that tag is used as the version.
> If the currently checked out revision is not tagged, then we take the last tagged
> version number and increment it to get a minimum target version.


### Commits

A `.devX` version will be incremented for every commit since the last version tag.

```
$ python3 setup.py --version
0.0.1.dev5
$ git add scratch.md; git commit -m "Adding scratch file"
...
$ python3 setup.py --version
0.0.1.dev6
$ git tag 0.1.0
0.1.0
```

Adding a commit with a `Sem-Ver: <keyword>` header will bump the version number depending on the keyword.

- No Sem-Ver header: patch bump
- `Sem-Ver: bugfix`: patch bump
- `Sem-Ver: deprecation`: minor bump
- `Sem-Ver: feature`: minor bump
- `Sem-Ver: api-break`: major bump



### Tags


### Builds

The following commands trigger PBR.

```
# Installation
pip install .

# Building
python -m build
```


