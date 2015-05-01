from bson.objectid import ObjectId
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

import agileid


def to_hexstring_invalid():
    return agileid.to_hexstring('rar')


def to_hexstring_invalid_oid():
    oid = str(ObjectId())
    return agileid.to_hexstring('user!' + oid)


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_cast_aid(self):
        aid = 'VUKNcId-tiJpAMRH'
        oid = '55428d70877eb6226900c447'

        self.assertEqual(agileid.to_hexstring(aid), oid)

    def test_cast_aid_scoped(self):
        aid = 'user!VUKNcId-tiJpAMRH'
        oid = '55428d70877eb6226900c447'

        self.assertEqual(agileid.to_hexstring(aid), oid)

    def test_cast_oid(self):
        oid = ObjectId()
        self.assertEqual(agileid.to_hexstring(oid), str(oid))

    def test_cast_oid_str(self):
        oid = str(ObjectId())
        self.assertEqual(agileid.to_hexstring(oid), oid)

    def test_cast_aid_invalid(self):
        self.assertRaises(ValueError, to_hexstring_invalid)

    def test_cast_aid_invalid_oid(self):
        self.assertRaises(ValueError, to_hexstring_invalid_oid)


if __name__ == '__main__':
    unittest.main()
