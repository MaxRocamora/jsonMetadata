# -*- coding: utf-8 -*-


class MissingJson(Exception):
    ''' Raise when system ask for a missing json file '''


class InvalidJson(Exception):
    ''' Raise when system cannot read a json file '''
