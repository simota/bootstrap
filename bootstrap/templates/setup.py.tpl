# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def get_readme():
    with open('README.rst') as f:
        return f.read()


def get_license():
    with open('LICENSE') as f:
        return f.read()

setup(
    name='{{ name }}',
    version='{{ version }}',
    description='{{ description }}',
    long_description=get_readme(),
    author='{{ author }}',
    author_email='{{ email }}',
    url='{{ url }}',
    license=get_license(),
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
)
