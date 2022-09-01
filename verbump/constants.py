# flake8:noqa

V_MAJOR = "major"
V_MINOR = "minor"
V_PATCH = "patch"
V_BUILD = "build"
version_parts = (V_MAJOR, V_MINOR, V_PATCH, V_BUILD)

presets = {
    "file:VERSION": {
        "pattern": r"""(\d+.\d+.\d+(?:.\d+)?)""",
    },
    "file:package.json": {
        "pattern": r"""(\d+.\d+.\d+(?:.\d+)?)""",
    },
    "file:*/__init__.py": {
        "pattern": r"""__version__\s*=\s*(?:"|')(\d+.\d+.\d+(?:.\d+)?)(?:"|')"""
    },
}
commit_format = "v%s"
tag_format = "v%s"
