# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def get_readme():
    with open('README.rst') as f:
        return f.read()


def get_license():
    with open('LICENSE') as f:
        return f.read()


setup(
    name='bootstrap',
    version='0.1.0',
    description='python package skeleton generator',
    long_description=get_readme(),
    author='simota',
    author_email='simota@me.com',
    url='https://github.com/simota/bootstrap',
    license=get_license(),
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=[
          'click>=6.7',
          'Jinja2>=2.10',
          'MarkupSafe>=1.0'
    ],
    entry_points={
        'console_scripts': [
            'bootstrap = bootstrap.cli:main',
        ],
    },
)
