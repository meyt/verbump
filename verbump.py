#!/usr/bin/python3
import os
import re
import sys
import subprocess
import configparser

from os.path import abspath, join

__version__ = "0.1.1"


class Version:
    major = 0
    minor = 1
    patch = 2
    build = 3


# TODO
# flake8: noqa
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


def git_call(*args):
    return subprocess.run(["git"] + list(args), stdout=subprocess.PIPE)


def git_has_stage():
    return git_call("diff", "--cached", "--exit-code").returncode == 1


def git_commit(version_filepath, version):
    # TODO custom format
    if git_has_stage():
        sys.exit("Stage must be empty")
    git_call("add", version_filepath)
    return git_call("commit", "-m", "v%s" % version)


def git_tag(version):
    # TODO custom format
    return git_call("tag", "v%s" % version)


def main():
    cwd = os.getcwd()
    config = configparser.ConfigParser()
    config.read(join(cwd, ".verbump.ini"))
    args = sys.argv
    part = getattr(Version, args[1]) if len(args) > 1 else Version.patch

    committed = False
    tagged = False
    for section in config.sections():
        version_filepath = abspath(section.split(":")[1])
        pattern = config.get(section, "pattern")
        with open(version_filepath) as f:
            content = f.read()

        current_version = None
        new_version = None

        def replacer(m):
            nonlocal current_version, new_version

            version = m.group(1)
            if not version:
                sys.exit("The regex pattern has no group")

            full_span = m.span(0)
            span = m.span(1)
            current_version = version
            version = list(map(int, version.split(".")))
            for k in range(len(version)):
                if k == part:
                    version[k] += 1

                elif k > part:
                    version[k] = 0

            new_version = ".".join(map(str, version))
            return (
                content[full_span[0] : span[0]]
                + new_version
                + content[span[1] : full_span[1]]
            )

        new_content = re.sub(pattern, replacer, content)

        if new_content == content:
            sys.exit("Cannot find version string")

        print("Version bump from %s to %s" % (current_version, new_version))

        with open(version_filepath, "w") as f:
            f.write(new_content)

        # git
        need_commit = config.get(section, "commit")
        if not committed and need_commit and need_commit.lower() == "true":
            git_commit(version_filepath, new_version)
            print("Committed %s" % new_version)
            committed = True

        need_tag = config.get(section, "tag")
        if not tagged and need_tag and need_tag.lower() == "true":
            git_tag(new_version)
            print("Tagged %s" % new_version)
            tagged = True


if __name__ == "__main__":
    main()
