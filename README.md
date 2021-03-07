# hello-pypi

Exploring PyPI packaging for CLI tools from scratch.


## How To Configure

### Create Build Files

Create these files
- `pyproject.toml`: Defines the build system, build dependencies, and other metadata. 
- `setup.cfg`: Static metadata. `setup.py` is for dynamic metadata, and should
    be avoided if possible.

Add a block to `setup.cfg` that defines a CLI command, and the corresponding
package function to call. Make sure to use `_` and not `-` in path names.
Below defines the command `hello-pypi` to execute the function `main()`,
in the module `hello_pypi.cli`.

```
[options.entry_points]
console_scripts =
    hello-pypi = hello_pypi.cli:main
```

## How To Install and Run Locally

Create a virtualenv (if needed).

```
python3 -m venv ./.venv
source .venv/bin/activate
```

Install the build dependencies.

```
python -m pip install --upgrade pip
pip install setuptools wheel build
```

Install the package locally.

```
pip install .
```

Run the command. It will only be available in the virtualenv (if used).

```
$ hello-pypi 
Hello PyPI!
```


## How To Release Manually

### Create PyPI Account and Token

Create an account on the test instance of PyPI: https://test.pypi.org/
The production instance of PyPI uses a separate account.

> TestPyPI – a separate instance of the Python Package
> Index that allows you to try distribution tools and processes without affecting
> the real index. 

Create a test PyPI API token: https://test.pypi.org/manage/account/token/


### Configure Environment

Set the environment variables with your API token.

```
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

Create virtualenv (if needed).

```
python3 -m venv ./.venv
source .venv/bin/activate
```


### Install Dependencies

Install build dependencies.

```
python -m pip install --upgrade pip
pip install setuptools wheel build twine
```

Install package dependencies.

```
pip install -r requirements.txt
```


### Build

Create the distribution

```
python -m build
```

A `./dist` subdirectory will be created, if not present, with the distribution files.
- `package_name-x.y.z-py3-none-any.whl`: Built distribution
- `package_name-x.y.z.tar.gz`: Source archive


### Deploy to Test PyPI

Install Twine and use it to upload the package to the test PyPI instance.
This command will read the user and API token from the `TWINE_USERNAME` and
`TWINE_PASSWORD` environment variables.

```
python3 -m twine upload --repository testpypi dist/*
```


### Install from Test PyPI

Install the test package.

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps js-hello-pypi 
```

Run the command. It will only be available in the virtualenv (if used).

```
$ hello-pypi 
Hello PyPI!
```

