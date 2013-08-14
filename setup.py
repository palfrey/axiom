import re
import setuptools

versionPattern = re.compile(
    r"__version__ = Version\("
    "\"(?P<name>\w*)\", "
    "(?P<major>\d*), "
    "(?P<minor>\d*), "
    "(?P<micro>\d*)\)")

with open("axiom/_version.py", "rt") as f:
    match = versionPattern.search(f.read())
    name, major, minor, micro = match.groups()
    print name, major, minor, micro

setuptools.setup(
    name=name,
    version=".".join([major, minor, micro]),
    description="An in-process object-relational database",
    url="http://divmod.org/trac/wiki/DivmodAxiom",

    maintainer="Divmod, Inc.",
    maintainer_email="support@divmod.org",

    packages=setuptools.find_packages() + ["twisted.plugins"],
    scripts=['bin/axiomatic'],

    license="MIT",
    platforms=["any"],

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Twisted",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Database"])
