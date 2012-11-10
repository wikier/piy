#!/usr/bin/python
# -*- coding: utf-8 -*-

import piy
from setuptools import setup

setup(
    name = "piy",
    version = piy.__version__,
    description = "POM in YAML",
    author = piy.__authors__,
    author_email = piy.__contact__,
    long_description = open("README.md", "r").read(),
    url = piy.__url__,
    packages = [
        "piy"
    ],
    requires = [
        "pyyaml",
        "hutools"
    ],
    install_requires = [
        "pyyaml",
        "hutools"
    ],
    package_data = {
        "rubber": []
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: " + piy.__license__,
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities"
    ],
    entry_points = {
        "console_scripts" : [
            "piy = piy:transform_pom_yaml_to_xml"
        ]
    }
)

