import unittest

from data_structures.stack import Stack
from data_structures.exceptions import StackEmptyError
from data_structures.exceptions import StackLimitReachedError


class StackTest(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack(max_size=5)

    def test_created_empty_stack(self) -> None:
        self.assertEqual(self.stack.size, 0)

    def test_push_one_element(self) -> None:
        self.stack.push(10)
        self.assertEqual(self.stack.size, 1)

    def test_push_three_elements(self) -> None:
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.size, 3)

    def test_pop_one_element(self) -> None:
        self.stack.push(10)
        
        element = self.stack.pop()
        self.assertEqual(element, 10)

    def test_empty_stack_after_pop_elements(self) -> None:
        self.stack.push(10)
        self.stack.push(20)

        _ = self.stack.pop()
        _ = self.stack.pop()

        self.assertEqual(self.stack.size, 0)

    def test_raise_empty_stack_exception(self) -> None:
        self.stack.push(10)
        _ = self.stack.pop()

        self.assertRaises(StackEmptyError, self.stack.pop)

    def test_raise_limit_reached_exception(self) -> None:
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.stack.push(40)
        self.stack.push(50)

        self.assertRaises(StackLimitReachedError, self.stack.push, 60)
