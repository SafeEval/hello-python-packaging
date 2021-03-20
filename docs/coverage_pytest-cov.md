
# Code Coverage: PyTest-Cov

## Installation

```
pip install pytest-cov
```

## Usage

Basic code coverage.

```
pytest --cov
```

Code coverage with a defined configuration file, that exports to HTML.

```
pytest --cov-config=.coveragerc --cov=hello_pp hello_pp/tests/ --cov-report html
```

## Configuration

Specify a coverage configuration in `.coveragerc`. This will ignore all `__init__.py` files and the `__version__.py` file.

```
[run]
omit = */__*__.py
```

Configure `pytest` to use the configuration automatically in `setup.cfg`.

```
[tool:pytest]
addopts = --cov-config=.coveragerc --cov=hello_pp --cov-report html
```

Running `pytest` will also run coverage, and generate the HTML report in the `htmlcov` folder.


## Resources

https://pytest-cov.readthedocs.io/en/latest/config.html
