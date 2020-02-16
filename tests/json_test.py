# coding=utf-8
from __future__ import absolute_import, print_function

import unittest
import os

from jsonmd.json_metadata import JsonMetadata

test_path = os.path.join(os.path.dirname(__file__), 'test_files')
test_name = 'test'


class Test_windows(unittest.TestCase):

    def test_create_and_save(self):
        meta = JsonMetadata(test_name)

        # test properties
        self.assertEqual(meta.name, test_name)
        meta.version
        meta.data
        meta.extension
        meta.prefix
        meta.path
        meta.filepath
        meta.filename
        meta.has_file
        meta.system

        meta.path = test_path
        # check if path is equal to abspath

        # check if filepath is equal to abspath + filename + suffix + ext

        meta.insert(key='coins', value=12)

        # check if data have coins and value 12
        print(meta.data['coins'])
        meta.save()

        # check if file exists

        # meta.update({'coins': 7})
        meta.insert(key='coins', value=7)

        # check if data have coins and value 7

        meta.remove('coins')
        # check if coins is deleted
        print(meta.data.get('coins', None))

        meta.insert(key='guns', value=['colt', 'magnum'])
        meta.save()
        metaObj = meta.load_as_class()
        print(metaObj)
        print(metaObj.guns)

        # save_from_a_class
        # self.assertEqual(asset._id, DEFAULT_ASSET_IDENTIY,
        #                  'Asset _id is {}, must be {}'.format(asset._id, DEFAULT_ASSET_IDENTIY))


if __name__ == '__main__':
    unittest.main()
