from typing import Any

from data_structures.exceptions import BinaryTreeLimitReachedError


class TreeNode:
    def __init__(self, value: int) -> None:
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.value = value


class BinaryTree:
    def __init__(self, max_size: int = None) -> None:
        self.size = 0
        self.root = None
        self.max_size = max_size

    def __add_helper(self, node: TreeNode, value: int) -> None:
        if value < node.value:
            if node.left is None:
                self.size += 1
                node.left = TreeNode(value)
            else:
                self.__add_helper(node.left, value)
        else:
            if node.right is None:
                self.size += 1
                node.right = TreeNode(value)
            else:
                self.__add_helper(node.right, value)

    def add(self, value: int) -> None:
        if self.max_size is not None:
            if self.size == self.max_size:
                raise BinaryTreeLimitReachedError()

        if self.root is None:
            self.root = TreeNode(value)
            self.size += 1
        else:
            self.__add_helper(self.root, value)

    def __find_helper(self, node: TreeNode, value: int) -> bool:
        if node.value == value:
            return True
        elif node.left is not None:
            return self.__find_helper(node.left, value)
        elif node.right is not None:
            return self.__find_helper(node.right, value)
        
        return False

    def find(self, value: int) -> bool:
        if self.root is None:
            return False
        
        return self.__find_helper(self.root, value)

    def __height_helper(self, node: TreeNode) -> int:
        if node is None:
            return 0

        return 1 + max(self.__height_helper(node.left), self.__height_helper(node.right))

    def height(self) -> int:
        return self.__height_helper(self.root)
