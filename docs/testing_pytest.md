# Testing: PyTest

## Installation

```
pip install pytest
```

## Usage

Run `pytest` across current and sub-folders.

```
pytest
```

Run `pytest` across specified folder.

```
pytest ./tests/
```

Any Python modules with the naming convention `test_*.py` or `*_test.py` will be executed. This allows tests to be isolated in a `./tests/` folder, separate from the source code.


## Configuration

Can configure `pytest` in a `setup.cfg` block.

```
[tool:pytest]
addopts = --cov-config=.coveragerc --cov=hello_pp --cov-report html
```

Can also use the `pytest.ini` file to configure how `pytest` behaves.

```
[pytest]
addopts = --cov-config=.coveragerc --cov=hello_pp --cov-report html
```

## Resources

https://realpython.com/pytest-python-testing/
