from bson.objectid import ObjectId
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

import agileid


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_cast_aid(self):
        aid = 'VUKNcId-tiJpAMRH'
        oid = ObjectId('55428d70877eb6226900c447')
        self.assertEqual(agileid.to_objectid(aid), oid)

    def test_cast_oid(self):
        oid = ObjectId()
        self.assertEqual(agileid.to_objectid(oid), oid)

    def test_cast_oid_str(self):
        oid = ObjectId()
        self.assertEqual(agileid.to_objectid(str(oid)), oid)


if __name__ == '__main__':
    unittest.main()
