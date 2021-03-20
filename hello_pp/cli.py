#!/usr/bin/env python3
"""
Top level CLI module.
"""

from .__version__ import __version__


def main():
    """ CLI entrypoint.
    """
    print(f'Hello Python Project! ({__version__})')


def untested():
    """ Untested function for code coverage.
    """
    print('This function is untested. Will show up in code coverage.')
