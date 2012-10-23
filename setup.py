#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import warnings
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)


with warnings.catch_warnings():
    warnings.simplefilter("ignore")

setup(
    name = "liststyle",
    description = "Style your django admin changelist rows with ease!",
    long_description = open('README').read(),
    url = "https://github.com/s29/django-liststyle",
    packages = find_packages(),
    package_data = {
            '': ['README', ],
                },
    include_package_data=True,
    zip_safe=True,
)

