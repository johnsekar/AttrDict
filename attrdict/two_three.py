"""
Support for python 2/3.

NOTE: If you make changes to this, please manually run flake8 against
    it. tox/travis skip this file as basestring is undefined in Python3.
"""
from sys import version_info


if version_info < (3,):
    PYTHON_2 = True
    StringType = basestring

    def iteritems(mapping):
        """
        Iterate over a mapping object.
        """
        return mapping.iteritems()
else:
    PYTHON_2 = False
    StringType = str

    def iteritems(mapping):
        """
        Iterate over a mapping object.
        """
        return mapping.items()