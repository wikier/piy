#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="piy",
    version="0.0.1",
    description="POM in YAML",
    author="Sergio Fernández",
    author_email="sergio@wikier.org",
    long_description=open("README.md", "r").read(),
    url="http://github.com/wikier/piy",
    packages=[
        "piy"
    ],
    requires=[
        "yaml",
        "hutools"
    ],
    install_requires=[
        "yaml",
        "hutools"
    ],
    package_data={
        "rubber": []
    },
    test_suite="tests",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities"
    ],
)

