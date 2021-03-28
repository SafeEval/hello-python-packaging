# Python Linting: Black

Black is an opinionated Python linter and automated code formatter,
with intentionally few options. It's goal is to standardize how Python
code in projects is formatted.

## Pre-Commit Hook

In `.pre-commit-config.yaml`, add an entry for `black`.

```
-   repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
    -   id: black
```

## Github Actions

Create a linting workflow (if one doesn't exist) in
`.github/workflows/lint.yaml`,and add `black`.

```
name: lint

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - uses: psf/black@stable
        with:
          args: ". --check"
```
