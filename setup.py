#!/usr/bin/env python
import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_simpletasks',
    version='0.1',
    packages=['simpletasks'],
    include_package_data=True,
    license='MIT License',
    description='Simple background and scheduled tasks for Django.',
    author='Henrik Heino',
    author_email='henrik.heino@gmail.com',
    install_requires=[
    ],
    dependency_links=[
    ],
)
