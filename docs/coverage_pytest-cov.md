
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

Running `pytest` will also run coverage, and generate the HTML report in the
`htmlcov` folder.

### Resources for Pytest

https://pytest-cov.readthedocs.io/en/latest/config.html


## Code Climate Coverage Reports

Code Climate can receive and track code coverage reports.
These won't show up in the project dashboard, until a coverage report is uploaded
for the default branch (i.e. `main`).

To allow uploading and tracking of coverage in Code Climate, set the coverage output
format to XML in `setup.cfg`. A `coverage.xml` file will be generated instead of HTML.

```
[tool:pytest]
addopts = --cov-config=.coveragerc --cov=hello_pp --cov-report xml
```

### Upload Manually

Download the static binary from Code Climate, `cc-test-reporter`.

Find the test reporter ID in Code Climate, then run these commands:

```
# Set the test reporter ID.
export CC_TEST_REPORTER_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Prepare the coverage.
cc-test-reporter before-build

# Run the tests.
pytest

# Upload the generated coverage/codeclimate.json file.
cc-test-reporter after-build --coverage-input-type=coverage.py
```

The report will be under "coverage" in the dashboard, where the test
reporter ID was located.


### Upload with Github Actions

Coverage reports can be uploaded to Code Climate, using Github Actions.

In Code Climate, go to the "coverage" section and find the "Test Reporter ID."
Set that value in the Github repositories secrets as `CC_TEST_REPORTER_ID`.

Below is a full workflow that runs `pytest` and uploads the code coverage report to Code Climate.


```
name: test

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    name: pytest
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@main
    - uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install testing dependencies
      run: pip install pytest pytest-cov

    - name: Test & publish code coverage
      uses: paambaati/codeclimate-action@v2.7.5
      env:
        CC_TEST_REPORTER_ID: ${{secrets.CC_TEST_REPORTER_ID}}
      with:
        coverageCommand: pytest
        coverageLocations: |
          ${{github.workspace}}/coverage.xml:coverage.py
        debug: true
```

### Enforcing Coverage

If enabled, Code Climate will report back to the PR if the latest commit
acheived the coverage threshold, and/or if the latest commit reduced coverage.

Excerpts are from the Code Climate [Test Coverage docs](https://docs.codeclimate.com/docs/configuring-your-analysis#test-coverage).

Enforce Diff Coverage: fail if new code has less than X% coverage

> The Enforce Diff Coverage option requires all new code in a Pull Request to
> meet a configurable minimum threshold of test coverage percentage. The
> default threshold is 50%.

Enforce Total Coverage: fail if all total coverage decreases by too much all at once(?).

> The Enforce Total Coverage option sends a pass/fail status based on whether
> the PR would have a positive/negative impact on the repository's overall test
> coverage.


The better check is Eforce Diff Coverage. It ensures that contributor's new code is tested at the configured threshold.

From experiments, the Eforce Total Coverage check an be bypassed if a developer pushes commits that lower the coverage by a little bit each time.

### Resources for Code Climate
https://docs.codeclimate.com/docs/configuring-test-coverage

https://docs.codeclimate.com/docs/configuring-test-coverage#list-of-subcommands

https://docs.codeclimate.com/docs/test-coverage-troubleshooting-branch-names

https://docs.codeclimate.com/docs/github-actions-test-coverage

https://github.com/marketplace/actions/code-climate-coverage-action


## Codecov Coverage Reports

The Codecov service can receive coverage reports for public repositories
without using a token for uploading, solving the lack of choice between
exposing secrets in unprivileged contexts or not enforcing coverage checks.

Key points:
- To generate a baseline, a coverage report needs to be uploaded from the default branch.
- Triggering on `push` will upload new baseline reports from default each time a PR is merged.

### Github Actions Workflow

Create a workflow that will upload a baseline coverage report to Codecov on merge to main.

```
name: Merge to Main

on:
  push:
    branches:
      - main

jobs:

  coverage:
    name: Baseline coverage report
    runs-on: ubuntu-latest
    steps:

    - uses: actions/checkout@main

    - uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install testing dependencies
      run: pip install pytest pytest-cov

    - name: Run tests
      run: pytest --cov-config=.coveragerc --cov=hello_pp

    - name: Upload coverage
      uses: codecov/codecov-action@v1
      with:
        fail_ci_if_error: true
```

Create a workflow that will run tests and upload coverage reports on any PR.

```
name: Pull Request

on: [pull_request]

jobs:

  test:
    name: Test
    runs-on: ubuntu-latest
    steps:

    - uses: actions/checkout@main

    - uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install testing dependencies
      run: pip install pytest pytest-cov

    - name: Run tests
      run: pytest --cov-config=.coveragerc --cov=hello_pp

    - name: Upload coverage
      uses: codecov/codecov-action@v1
      with:
        fail_ci_if_error: true
```

### Resources for Codecov

Codecov service:
- https://about.codecov.io/

Codecov docs:
- https://docs.codecov.io/docs/quick-start
- https://docs.codecov.io/docs/common-recipe-list
- https://docs.codecov.io/docs/supported-languages

Github Actions:
- https://github.com/codecov/example-python
- https://github.com/marketplace/actions/codecov
- https://github.com/codecov/codecov-action
