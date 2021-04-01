# -*- coding: utf-8 -*-
# setup file for trytrytry
# Learn more: https://github.com/janusson/trytrytry/README.md

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='trytrytry',
    version='0.1.0',
    description='Simple game in Python for weekend code sprint.',
    long_description=readme,
    author='Eric Janusson',
    author_email='ericjanusson@outlook.com',
    url='https://github.com/janusson/trytrytry',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
