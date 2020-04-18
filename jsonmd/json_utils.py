# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------
#
# Methods that handles commons json operations.
#
# 12/2017
# 03/2018 - Fix invalid json files
# 10/2018 - Moved from class to direct import methods
# 04/2020 - left only the 2 methods I use
# --------------------------------------------------------------------------------------------

from __future__ import absolute_import, print_function

import json
import os
from error import MissingJson, InvalidJson


def load_json(json_file):
    ''' returns a dict from json file
    Args:
        json_file (path) file to read data.
    '''
    if not os.path.exists(json_file):
        raise MissingJson(
            "json file not found ({}).".format(json_file))

    fIn = open(json_file, 'r')
    try:
        value = json.load(fIn)
    except ValueError as e:
        msg = "{} \n JSON File issue: {}".format(json_file, str(e))
        raise InvalidJson(msg)
    finally:
        fIn.close()

    return value


def save_json(dataDict, json_file):
    ''' Saves a dictionary into a json file
    Args:
        dataDict (dictionary) dictionary to save
        json_file (file) target file to save into
    '''

    if not os.path.dirname(json_file):
        os.makedirs(json_file)

    try:
        with open(json_file, 'w') as loadedJsn:
            json.dump(dataDict, loadedJsn, sort_keys=True, indent=4)
    except IOError:
        print('IOError: No such file of directory:', json_file)
