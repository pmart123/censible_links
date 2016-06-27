#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='censible_links',
      packages=find_packages(where='censible_links'),
      package_dir={"": "censible_links"},
      version='0.0.1',
      description='Crawl Censible.',
      url='https://github.com/pmart123/censible_links',
      author='Philip Martin',
      author_email='philip.martin@censible.co',
      install_requires=list(open('requirements.txt').read().strip().split('\r\n')),
      zip_safe=False)
