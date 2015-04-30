import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))

import agileid

# print agileid.create()


def create_invalid_scope():
    return agileid.create('huzzah!')


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_create(self):
        aid = agileid.create()
        self.assertEqual(len(aid), 16)

    def test_create_scoped(self):
        aid = agileid.create('user')
        self.assertEqual(len(aid), 21)
        self.assertTrue(aid.startswith('user!'))

    def test_create_scoped_invalid(self):
        self.assertRaises(ValueError, create_invalid_scope)


if __name__ == '__main__':
    unittest.main()
