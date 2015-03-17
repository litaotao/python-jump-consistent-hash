from __future__ import print_function

import sys

from setuptools import setup


if sys.version_info < (3, 2):
    print('ERROR: jump-consistent-hash requires Python version 3.2 or newer.',
          file=sys.stderr)
    sys.exit(1)


setup(name='jump_consistent_hash',
      version='1.0.1',
      description='Implementation of the Jump Consistent Hash algorithm',
      author='Peter Renström',
      license='MIT',
      url='https://github.com/renstrom/python-jump-consistent-hash',
      packages=['jump'],
      test_suite='tests',
      keywords=[
          'jump hash',
          'jumphash',
          'consistent hash',
          'hash algorithm',
          'hash'
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.4'
      ])
