import subprocess


def run(*args):
    return subprocess.run(["git"] + list(args), stdout=subprocess.PIPE)


def has_stage():
    return run("diff", "--cached", "--exit-code").returncode == 1


def add(filepath):
    return run("add", filepath)


def commit(message):
    return run("commit", "-m", message)


def tag(name):
    return run("tag", name)
