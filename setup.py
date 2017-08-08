# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""Pytest-Firefox setup file for packaging."""

from setuptools import setup

setup(name='pytest-firefox',
      use_scm_version=True,
      description='pytest plugin to manipulate firefox',
      long_description=open('README.rst').read(),
      author='Benjamin Forehand Jr',
      author_email='bforehand@mozilla.com',
      url='https://github.com/jrbenny35/pytest-firefox',
      packages=['pytest_firefox'],
      install_requires=[
          'FoxPuppet>=1.0.0',
          'pytest>=3.0.2',
          'selenium>=3.4.0'],
      setup_requires=['setuptools_scm'],
      entry_points={'pytest11': [
        'firefox = pytest_firefox.pytest_firefox']},
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest foxpuppet firefox mozilla automation selenium',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Pytest',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy'])
