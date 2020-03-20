import unittest
from tree import Tree


class TestNode(unittest.TestCase):
    def setUp(self):
        self.my_tree = Tree(5,Tree(3, Tree(2), Tree(5)),Tree(7, Tree(1), Tree(0, Tree(2), Tree(8, None, Tree(5)))))
        self.my_median = 4.0
        self.my_mean = 3.8
        self.my_sum = 38
        self.str_my_tree = "[5[3[2[][]][5[][]]][7[1[][]][0[2[][]][8[][5[][]]]]]]"

    def test_str_representation(self):
        self.assertEqual(self.my_tree.__str__(), self.str_my_tree)

    def test_positive_median_calculation(self):
        self.assertEqual(self.my_tree.median_value(), self.my_median)

    def test_positive_sum_calculation(self):
        self.assertEqual(self.my_tree.sum_subtree_values(), self.my_sum)

    def test_positive_mean_calculation(self):
        self.assertEqual(self.my_tree.mean_value(),self.my_mean)
