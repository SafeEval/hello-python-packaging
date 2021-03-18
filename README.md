[![Maintainability](https://api.codeclimate.com/v1/badges/a31efb881a1146ccf298/maintainability)](https://codeclimate.com/github/SafeEval/hello-python-packaging/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a31efb881a1146ccf298/test_coverage)](https://codeclimate.com/github/SafeEval/hello-python-packaging/test_coverage)

# Hello: Python Project

Exploring Python package builds, versioning, releases, pipelines, and
everything else that make a quality Python project "go."


## Things to Explore

- [x] Releasing (Python Semantic Release)
- [x] Automatic versioning (Python Semantic Release)
- [x] Automatic changelogs (Python Semantic Release)
- [ ] Enforcing Conventional Commit messages
- [ ] Pytest tests
- [ ] Tox tests
- [ ] Coverage
- [x] Linting (Code Climate)
- [x] SAST (Semgrep)
- [x] SCA (Snyk)
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

