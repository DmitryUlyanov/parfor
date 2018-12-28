#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='parfor',
      version='0.1',
      packages=['parfor'],
      package_dir={'parfor': 'parfor'},
      install_requires = ['tqdm', 'joblib'],
     )