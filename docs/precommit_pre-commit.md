# Pre-Commit Hooks: pre-commit

The `pre-commit` Python package looks for the `.pre-commit-config.yaml`
configuration file, and runs the defined pre-commit hooks.

Hooks are defined in, and cloned from, remote Git repositories.

This tool is not limited to Python projects. The package can be installed
globally, and used in any project.

Installation and configuration instructions in the documentation are
simple and clear: https://pre-commit.com/#quick-start


## Summarized Instructions

### Installation

1. Configure the `.pre-commit-config.yaml` file.
2. Install the package: `pip install pre-commit`
3. Use the package to install the hooks: `pre-commit install`
4. Manually run hooks on all files: `pre-commit run --all-files`
5. Continue regular flow. By default, hooks will be run on commit and push.

### New Hooks

1. Add the hook to the `.pre-commit-config.yaml` file.
2. Use the package to install the hooks: `pre-commit install`
3. Manually run hooks on all files: `pre-commit run --all-files`


## Configuration

Configuration keywords: https://pre-commit.com/#adding-pre-commit-plugins-to-your-project

Example `.pre-commit-config.yaml` file.

```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
    -   id: black
```

Keywords in the example:

- `repo`: The repository url to git clone from.
- `rev`: The revision or tag to clone at.
- `hooks`: A list of hook mappings.


## Helpful Hooks

A comprehensive list of hooks can be found here: https://pre-commit.com/hooks.html

Custom hooks can also be created.


### pre-commit-hooks

General hooks:

- `no-commit-to-branch`: Protect specific branches from direct checkins.
- `pretty-format-json`: auto-format and enforce pretty JSON files.
- `check-json`: verify JSON syntax.
- `check-xml`: verify XML syntax.
- `check-yaml`: verify YAML syntax.
- `check-toml`: verify TOML syntax.

Python specific hooks:

- `check-ast`: verify Python syntax.
- `debug-statements`: ensure no `breakpoint` statements are present.

Secrets scanning hooks:

- `detect-aws-credentials`: prevent AWS credentials.
- `detect-private-key`: prevent private keys.

### pre-commit-hooks-nodejs

General hooks:

- `markdown-toc`: insert a table of contents into markdown files.

### mypy

https://github.com/pre-commit/mirrors-mypy

- `mypy`: run mypy on a hook.

### black

- `black`: run black Python formatter on a hook.
