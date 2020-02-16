# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------
#
# Methods that handles commons json operations.
#
# v1 - 12/2017
# v2 - 03/2018 - Fix invalid json files
# v3 - 10/2018 - Moved from class to direct import methods
# --------------------------------------------------------------------------------------------

from __future__ import absolute_import, print_function

import json
import os
from .error import MissingOrInvalidJson


def get_single_json_value(json_file, value):
    ''' returns a single value from json file
    json_file (path) system file to read data.
    value (str) value from dictionary to query value
    '''
    if os.path.exists(json_file):
        fIn = open(json_file, 'r')
        try:
            jsonContainer = json.load(fIn)
        except ValueError, e:
            print ("JSON object issue: %s") % e
            fIn.close()
            return False
        fIn.close()
        value = jsonContainer.get(value)
        return value
    else:
        raise MissingOrInvalidJson(
            "json: Config File not found: {} for Value {}.".format(json_file, value))


def load_json(json_file):
    ''' returns a dict from json file
    json_file (path) system file to read data.
    '''
    import os
    import json
    if os.path.exists(json_file):
        fIn = open(json_file, 'r')
        try:
            value = json.load(fIn)
        except ValueError, e:
            fIn.close()
            raise OSError("{} \n JSON File issue: {}".format(json_file, str(e)))
        fIn.close()
        return value
    else:
        raise MissingOrInvalidJson(
            "get_json: Config File not found: {}.".format(json_file)
        )


def save_json(dataDict, json_file):
    ''' Saves a dictionary into a json file
    Args:
        dataDict (dictionary) dictionary to save
        json_file (file) target file to save into
    '''

    if not os.path.dirname(json_file):
        os.mkdir(json_file)

    try:
        with open(json_file, 'w') as loadedJsn:
            json.dump(dataDict, loadedJsn, sort_keys=True, indent=4)
    except IOError:
        print('IOError: No such file of directory:', json_file)


def update_json(values, json_file):
    ''' Opens a json file, load its params,
    add new keys and save it
    '''
    if not os.path.exists(json_file):
        dictData = {}
        with open(json_file, 'w') as loadedJsn:
            json.dump(dictData, loadedJsn, sort_keys=True, indent=4)

    # opens and read json into dictData
    with open(json_file, 'r') as loadedJsn:
        dictData = json.load(loadedJsn)
        dictData.update(values)

    with open(json_file, 'w') as loadedJsn:
        json.dump(dictData, loadedJsn, sort_keys=True, indent=4)
