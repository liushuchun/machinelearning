# coding: utf-8
import unittest

import trees


class TestTrees(unittest.TestCase):

    def setUp(self):
        print 'setUp ...'

    def tearDown(self):
        print 'tearDonw...'

    def test_init(self):
        pass

    def test_calculate_ent(self):

        data, label = trees.create_data()
        print trees.calc_shannon_ent(data)


if __name__ == "__main__":
    unittest.main()
