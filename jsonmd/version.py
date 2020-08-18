# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------
'''
1.0.0 - Release 1
1.1.0 - Cleaner errors and json_utils, some refactor
1.1.1 - Fixed pipinstall

'''

VERSION_MAJOR = 1
VERSION_MINOR = 1
VERSION_PATCH = 1

version = '{}.{}.{}'.format(VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)
__version__ = version

__app__ = 'Json Metadata'

__all__ = ['version', '__version__', '__app__']
