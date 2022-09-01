from setuptools import setup


def read_version(module_name):
    from re import match, S
    from os.path import join, dirname

    f = open(join(dirname(__file__), module_name, "__init__.py"))
    return match(r".*__version__ = (\"|')(.*?)('|\")", f.read(), S).group(2)


setup(
    name="verbump",
    version=read_version("verbump"),
    description="Easy version incrementing CLI tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="MeyT",
    url="http://github.com/meyt/verbump",
    license="MIT",
    keywords="version versioning semver",
    python_requires=">=3.5",
    packages=["verbump"],
    entry_points={"console_scripts": ["verbump = verbump.cli:main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],
)
