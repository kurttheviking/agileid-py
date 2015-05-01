from bson.objectid import ObjectId
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

import agileid


def cast_invalid_id():
    return agileid.cast('foo')


def cast_invalid_oid():
    return agileid.cast('user!54e2a40ea60b442fff000001')


def cast_invalid_type():
    return agileid.cast('VOKkDqYLRC__AAAB', 'bigco!user')


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_cast_aid(self):
        aid = agileid.cast('VOKkDqYLRC__AAAB')
        self.assertEqual(aid, 'VOKkDqYLRC__AAAB')

    def test_cast_aid_scoped(self):
        aid = agileid.cast('VOKkDqYLRC__AAAB', 'user')
        self.assertEqual(aid, 'user!VOKkDqYLRC__AAAB')

    def test_cast_aid_scoped_existing(self):
        aid = agileid.cast('user!VOKkDqYLRC__AAAB', 'user')
        self.assertEqual(aid, 'user!VOKkDqYLRC__AAAB')

    def test_cast_oid_basic(self):
        aid = agileid.cast(ObjectId())
        self.assertEqual(len(aid), 16)

    def test_cast_oid(self):
        aid = agileid.cast(ObjectId('54e2a40ea60b442fff000001'))
        self.assertEqual(aid, 'VOKkDqYLRC__AAAB')

    def test_cast_oid_str(self):
        aid = agileid.cast('54e2a40ea60b442fff000001')
        self.assertEqual(aid, 'VOKkDqYLRC__AAAB')

    def test_cast_oid_basic_scoped(self):
        aid = agileid.cast(ObjectId(), 'user')
        self.assertTrue(aid.startswith('user!'))
        self.assertEqual(len(aid), 21)

    def test_cast_oid_scoped(self):
        aid = agileid.cast(ObjectId('54e2a40ea60b442fff000001'), 'user')
        self.assertEqual(aid, 'user!VOKkDqYLRC__AAAB')

    def test_cast_oid_str_scoped(self):
        aid = agileid.cast('54e2a40ea60b442fff000001', 'user')
        self.assertEqual(aid, 'user!VOKkDqYLRC__AAAB')

    def test_cast_invalid(self):
        self.assertRaises(ValueError, cast_invalid_id)

    def test_cast_invalid_oid(self):
        self.assertRaises(ValueError, cast_invalid_oid)

    def test_cast_invalid_type(self):
        self.assertRaises(ValueError, cast_invalid_type)


if __name__ == '__main__':
    unittest.main()
