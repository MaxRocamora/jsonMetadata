# -*- coding: utf-8 -*-
'''

'''

from sys import executable
import os
import time
from datetime import datetime
import platform
from json_utils import load_json, save_json
from version import *


class JsonMetadata():
    ''' Json Metadata Class
    '''
    def __init__(self, name):
        self._name = name
        self._data = {}
        self._data["_about"] = 'Saved by JsonMetada'
        self._data["_version"] = version

    @property
    def version(self):
        ''' version '''
        return version

    @property
    def name(self):
        ''' name of this metadata class'''
        return self._name

    @property
    def data(self):
        ''' metadata info of the data dict '''
        return self._data

    @property
    def extension(self):
        ''' extension of the json file '''
        return ".json"

    @property
    def prefix(self):
        ''' file prefix, is autoincluded on the filename '''
        return "MD_"

    @property
    def filename(self):
        ''' Returns default filename with prefix and extension '''
        return self.prefix + self.name + self.extension

    @property
    def filepath(self):
        ''' full json metadata filepath '''
        return os.path.join(self.path, self.filename)

    @property
    def path(self):
        ''' base path location of metadata json file '''
        if not hasattr(self, '_path'):
            return os.path.dirname(__file__)
        return self._path

    @path.setter
    def path(self, val):
        self._path = os.path.realpath(val)

    @property
    def has_file(self):
        return os.path.exists(self.filepath)

# --------------------------------------------------------------------------------------------
# METADATA GET
# --------------------------------------------------------------------------------------------

    def load_as_class(self):
        ''' returns the metada dict as a class obj '''
        metadataClass = type(self.name, (), self._data)
        return metadataClass

    def load(self):
        ''' loads metadata from disk '''
        if self.has_file:
            self._data = load_json(self.filepath)
        else:
            self._data = {}

    def insert(self, key, value):
        ''' inserts value into metadata '''
        self._data[key] = value

    def remove(self, key):
        ''' remove key from metadata '''
        if key in self._data.keys():
            del self._data[key]

    def save(self):
        ''' Save current metadata into json file. '''
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        self.data = self._include_system_data(self.data)
        save_json(self.data, self.filepath)

# --------------------------------------------------------------------------------------------
# SYSTEM METADATA OS/USER/TIME
# --------------------------------------------------------------------------------------------

    @property
    def system(self):
        return self._include_system_data({})

    def _include_system_data(self, data):
        ''' add system metadata to the default data before save '''
        sys_data = {}
        sys_data['name'] = self.name
        sys_data['app'] = self._get_executable
        sys_data['PC'] = self._get_platform
        sys_data['User'] = self._get_user
        sys_data['time'] = self._get_time_metadata
        data['system'] = sys_data
        return data

    @property
    def _get_platform(self):
        ''' Get pc name '''
        return str(platform.node())

    @property
    def _get_user(self):
        ''' Get pc user '''
        return str(os.getenv('username'))

    @property
    def _get_time_metadata(self):
        ''' Get export time info. '''
        ftime = time.strftime("%Y,%b,%d,%j,%H:%M", time.localtime())
        times = ftime.split(",")
        td = {
            "year": times[0],
            "month": times[1],
            "day": times[2],
            "year_day": times[3],
            "time": times[4],
            'save_time': datetime.now().ctime()
        }
        return td

    @property
    def _get_executable(self):
        ''' Get source exec '''
        return os.path.basename(executable)
