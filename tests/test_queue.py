import unittest

from data_structures.queue import Queue
from data_structures.exceptions import QueueEmptyError
from data_structures.exceptions import QueueLimitReachedError


class QueueTest(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue(max_size=5)

    def test_created_empty_queue(self) -> None:
        self.assertEqual(self.queue.size, 0)

    def test_insert_one_element(self) -> None:
        self.queue.insert(10)
        self.assertEqual(self.queue.size, 1)

    def test_insert_three_elements(self) -> None:
        self.queue.insert(10)
        self.queue.insert(20)
        self.queue.insert(30)
        self.assertEqual(self.queue.size, 3)

    def test_remove_one_element(self) -> None:
        self.queue.insert(10)
        
        element = self.queue.remove()
        self.assertEqual(element, 10)

    def test_remove_elements_correct_order(self) -> None:
        self.queue.insert(10)
        self.queue.insert(20)
        self.queue.insert(30)

        first_element = self.queue.remove()
        second_element = self.queue.remove()
        third_element = self.queue.remove()

        self.assertEqual(first_element, 10)
        self.assertEqual(second_element, 20)
        self.assertEqual(third_element, 30)

    def test_empty_queue_after_remove_elements(self) -> None:
        self.queue.insert(10)
        self.queue.insert(20)

        _ = self.queue.remove()
        _ = self.queue.remove()

        self.assertEqual(self.queue.size, 0)

    def test_raise_empty_queue_exception(self) -> None:
        self.queue.insert(10)
        _ = self.queue.remove()

        self.assertRaises(QueueEmptyError, self.queue.remove)

    def test_raise_limit_reached_exception(self) -> None:
        self.queue.insert(10)
        self.queue.insert(20)
        self.queue.insert(30)
        self.queue.insert(40)
        self.queue.insert(50)

        self.assertRaises(QueueLimitReachedError, self.queue.insert, 60)
