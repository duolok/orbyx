#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup, find_packages

directory = Path(__file__).resolve().parent
with open(directory / 'requirements.txt') as f:
    dependencies = f.read()


setup(
    name='orbyx',
    version='0.0.1',
    packages=find_packages(),
    install_requires=dependencies,
)
