import unittest

from data_structures.binary_tree import BinaryTree
from data_structures.exceptions import BinaryTreeEmptyError
from data_structures.exceptions import BinaryTreeLimitReachedError
from data_structures.exceptions import ValueNotFoundInBinaryTreeError
from data_structures.exceptions import BinaryTreeNodeHasNotNullChildren


class BinaryTreeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinaryTree(max_size=5)

    def test_created_empty_binary_tree(self) -> None:
        self.assertEqual(self.tree.size, 0)

    def test_add_one_node(self) -> None:
        self.tree.add(10)
        self.assertEqual(self.tree.size, 1)

    def test_add_three_nodes(self) -> None:
        self.tree.add(10)
        self.tree.add(20)
        self.tree.add(30)
        self.assertEqual(self.tree.size, 3)

    def test_height_of_empty_tree(self) -> None:
        self.assertEqual(self.tree.height(), 0)

    def test_height_of_non_empty_tree(self) -> None:
        self.tree.add(5)
        self.tree.add(1)
        self.tree.add(8)
        self.tree.add(3)
        self.tree.add(6)

        self.assertEqual(self.tree.height(), 3)

    def test_find_existing_node(self) -> None:
        self.tree.add(5)
        self.tree.add(2)
        self.tree.add(10)
        self.tree.add(4)
        self.tree.add(11)
        self.assertTrue(self.tree.find(4))

    def test_find_non_existing_node(self) -> None:
        self.tree.add(2)
        self.tree.add(3)
        self.tree.add(10)
        self.tree.add(1)
        self.assertFalse(self.tree.find(4))

    def test_raise_limit_reached_exception(self) -> None:
        self.tree.add(10)
        self.tree.add(20)
        self.tree.add(30)
        self.tree.add(40)
        self.tree.add(50)
        self.assertRaises(BinaryTreeLimitReachedError, self.tree.add, 60)
