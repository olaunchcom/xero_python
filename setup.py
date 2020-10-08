#!/usr/bin/env python

"""The setup script."""
import re

from setuptools import setup, find_packages

COMMENT_RE = re.compile(r"(^|\s+)#.*$")


def load_requirements(file_name):
    requirements = []
    with open(file_name, "r") as req_file:
        for line in req_file:
            line = COMMENT_RE.sub("", line)
            line = line.strip()
            if line:
                requirements.append(line)
    return requirements


def read_file(filename):
    with open(filename) as fp:
        return fp.read()


setup(
    author="Xero Developer API",
    author_email="api@xero.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Official Python sdk for Xero API generated by OpenAPI spec for oAuth2",
    install_requires=load_requirements("requirements.txt"),
    license="MIT license",
    long_description="\n\n".join((read_file("README.md"), read_file("HISTORY.md"))),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="xero python sdk API oAuth",
    name="xero_python",
    packages=find_packages(include=["xero_python", "xero_python.*"]),
    version="1.0.11",
)
