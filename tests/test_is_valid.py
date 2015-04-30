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
        self.assertTrue(agileid.is_valid('VOKkDqYLRC__AAAB'))

    def test_cast_aid_scoped(self):
        self.assertTrue(agileid.is_valid('user!VOKkDqYLRC__AAAB'))

    def test_invalid(self):
        self.assertFalse(agileid.is_valid('foo'))

    def test_invalid_scope(self):
        self.assertFalse(agileid.is_valid('huzzah!!VOKkDqYLRC__AAAB'))

    def test_invalid_oid(self):
        self.assertFalse(agileid.is_valid(ObjectId()))

    # def test_invalid_id(self):
    #     self.assertRaises(ValueError, check_invalid_id)

    # def test_invalid_oid(self):
    #     self.assertRaises(ValueError, check_invalid_oid)


if __name__ == '__main__':
    unittest.main()
