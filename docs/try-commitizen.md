# Versioning with Commitizen


## Resources

https://github.com/commitizen-tools/commitizen

https://github.com/commitizen-tools/commitizen/blob/master/docs/bump.md


## Setup

Added configuration to `pyproject.toml`, and removed from `setup.cfg:metadata`.

```
[tool.commitizen]
tag_format = "v$minor.$major.$patch$prerelease"
version = "0.0.2"
```

