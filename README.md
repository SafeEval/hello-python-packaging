# hello-python-packaging

Exploring Python package builds, versioning, releases, pipelines, and
everything else that make a quality Python project "go."


## Things to Explore

- [x] Releasing
- [x] Automatic versioning
- [x] Automatic changelogs
- [ ] Enforcing Conventional Commit messages (for automatic versioning/changelogs)
- [ ] Pytest tests
- [ ] Tox tests
- [ ] Coverage
- [ ] Linting
- [ ] SAST
- [ ] SCA
- [ ] Contributing howto documentation
- [ ] Automated documentation


## Installation and Usage

### Setup Virtualenv (Optional)

Create a virtualenv (if needed).

```
python3 -m venv ./.venv
source .venv/bin/activate
```

### Install from Test PyPI

Install the test package from the test instance of PyPI.

```
pip install -i https://test.pypi.org/simple/ js-hello-python-packaging
```

### Install from Local Repo

Install the package locally.

```
pip install .
```

### Run the Command

Run the command. It will only be available in the virtualenv (if used).

```
$ hello-pp
Hello Python Packaging! (3.0.1)
```

