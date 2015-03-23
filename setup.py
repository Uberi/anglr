#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

import sys
if sys.version_info < (3, 2):
    print("THIS MODULE REQUIRES PYTHON 3.3 OR LATER. YOU ARE CURRENTLY USING PYTHON " + sys.version)
    sys.exit(1)

import anglr

setup(
    name="anglr",
    version=anglr.__version__,
    py_modules=["anglr"],
    include_package_data=True,

    # PyPI metadata
    author=anglr.__author__,
    author_email="azhang9@gmail.com",
    description=anglr.__doc__,
    long_description=open("README.rst").read(),
    license=anglr.__license__,
    keywords="angle angles radians unit convert",
    url="https://github.com/Uberi/anglr#readme",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
