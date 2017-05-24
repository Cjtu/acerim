from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 2 - Pre-Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Natural Language :: English",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "acerim: a package for classifying impact crater ejecta"
# Long description will go up on the pypi page
long_description = """

Acerim
========
Acerim is a package for identifying and classifying impact crater ejecta.

It contains functions and classes useful for loading image data and crater 
databases to classify, display and analyze impact crater ejecta quantitatively. 
This package was written with lunar maturity data in mind, but is general 
enough to be applicable to craters on any spherical body.

To get started using this software, please go to the repository README_.

.. _README: https://github.com/cjtu/acerim/master/README.md

License
=======
``acerim`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.

All trademarks referenced herein are property of their respective holders.

Copyright (c) 2017--, Christian Tai Udovicic.
"""

NAME = "acerim"
MAINTAINER = "Christian Tai Udovicic"
MAINTAINER_EMAIL = "cj.taiudovicic@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/cjtu/acerim"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Christian Tai Udovicic"
AUTHOR_EMAIL = "cj.taiudovicic@gmail.com"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'acerim': [pjoin('data', '*')]}
REQUIRES = ["numpy", "gdal", "pandas"]