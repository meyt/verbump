#!/usr/bin/python3
import os
import sys
import argparse
import configparser

from os.path import abspath, join, exists

from verbump import git, constants, version, __version__


def main():
    parser = argparse.ArgumentParser(
        description="Easy version incrementing CLI tool",
    )
    parser.add_argument(
        "part",
        type=str,
        default=constants.V_PATCH,
        nargs="?",
        help="Version part",
        choices=constants.version_parts,
    )
    parser.add_argument(
        "--version",
        action="version",
        version="verbump %s" % __version__,
    )
    parser.add_argument(
        "--config",
        "-c",
        default=join(os.getcwd(), ".verbump.ini"),
        help="Set config file",
    )
    args = parser.parse_args()

    config = configparser.RawConfigParser(
        defaults=dict(
            commit="false",
            tag="false",
            commit_format=constants.commit_format,
            tag_format=constants.tag_format,
        )
    )
    config.read(args.config)

    part = constants.version_parts.index(args.part)
    committed = False
    tagged = False
    for section in config.sections():
        verpath = abspath(section.split(":")[1])
        pattern = config.get(section, "pattern")

        if not exists(verpath):
            sys.exit("Cannot find version file '%s'" % verpath)

        # bump
        with open(verpath) as f:
            content, oldver, newver = version.bump(f.read(), pattern, part)

        print("Version bump from %s to %s on '%s'" % (oldver, newver, verpath))

        with open(verpath, "w") as f:
            f.write(content)

        # git commit
        need_commit = config.get(section, "commit")
        if not committed and need_commit and need_commit.lower() == "true":
            if git.has_stage():
                sys.exit("Stage must be empty")
            git.add(verpath)
            git.commit(config.get(section, "commit_format") % newver)
            print("Committed %s" % newver)
            committed = True

        # git tag
        need_tag = config.get(section, "tag")
        if not tagged and need_tag and need_tag.lower() == "true":
            git.tag(config.get(section, "tag_format") % newver)
            print("Tagged %s" % newver)
            tagged = True
