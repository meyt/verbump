# verbump

Easy version incrementing CLI tool.

* Automatic relative version detect and bump
* Automatic `git commit` and `git tag`
* Regex based configuration
* Using `semver` style

## Installation

```bash
pip install verbump
```

## Usage

1. Create `.verbump.ini` inside your project's root directory and put the configuration inside it.
2. Run `verbump`

```
verbump [major|minor|patch|build]
```

### Relative bump

```bash
verbump minor
```

## Configuration samples

### Generic `VERSION` file:

```ini
[file:VERSION]
pattern = (\d+.\d+.\d+(?:.\d+)?)*
```

### Generic `VERSION` file + GIT auto-commit & auto-tag:

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
