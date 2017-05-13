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
        ret = trees.split_data_set(data, 0, 1)
        print ret

    def test_choose_best_features(self):
        data, label = trees.create_data()
        self.assertEqual(trees.choose_best_feature_tosplit(data), 0)

    def test_create_tree(self):
        data, label = trees.create_data()

        myTree = trees.create_tree(data, label)

        print myTree

    def test_classify(self):
        data, label = trees.create_data()
        myTree = trees.retrieve_trees(0)

        print "here"
        print myTree
        self.assertEqual('no', trees.classify(myTree, label, [1, 0]))
        self.assertEqual('yes', trees.classify(myTree, label, [1, 1]))


if __name__ == "__main__":
    unittest.main()
