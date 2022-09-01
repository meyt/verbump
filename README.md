# verbump

[![pypi](https://img.shields.io/pypi/pyversions/verbump.svg)](https://pypi.python.org/pypi/verbump)

Easy version incrementing CLI tool.

* Automatic relative version bump
* Automatic `git commit` and `git tag`
* Regex based version pattern
* Using `semver` style

## Installation

```bash
pip install verbump
```

## Usage

1. Create the configuration file `.verbump.ini` inside your project's root directory.
2. Run `verbump`

```bash
verbump [major|minor|patch|build]
```

### Relative bump

```bash
verbump minor
```

## Configuration

Available keys for `.verdump.ini` :

* `pattern`: {string} Version pattern regex (required)
* `commit`: {boolean} Enables git auto-commit
* `tag`: {boolean} Enables git auto-tag
* `commit_format`: {string} Auto-commit message format. default is `v%s`
* `tag_format`: {string} Auto-tag name format. default is `v%s`

## Configuration samples

### Generic `VERSION` file:

```ini
[file:VERSION]
pattern = (\d+.\d+.\d+(?:.\d+)?)*
```

### Generic `VERSION` file, git auto-commit & auto-tag enabled:

```ini
[file:VERSION]
commit = true
tag = true
pattern = (\d+.\d+.\d+(?:.\d+)?)*
```

### Nodejs `package.json` :

```ini
[file:package.json]
pattern = "version"\s*:\s*"(\d+.\d+.\d+(?:.\d+)?)"\s*,
```

### Python `__version__` style:

```ini
[file:mymodule/__init__.py]
pattern = __version__\s*=\s*(?:"|')(\d+.\d+.\d+(?:.\d+)?)(?:"|')
```
