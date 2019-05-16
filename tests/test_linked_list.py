from unittest import TestCase
from linked_list import LinkedList
import unittest

class TestLinkedList(TestCase):
    def setUp(self):
        self.ll = LinkedList()
    def test_add_data(self):
        self.assertEqual(len(self.ll), 0)
        self.ll.add_data(4)
        self.assertEqual(len(self.ll), 1)
        self.ll.add_data(56)
        self.ll.add_data(67)
        self.assertEqual(self.ll._head.data, 4)
        self.assertEqual(self.ll._head.next.data, 56)
        self.assertEqual(self.ll._head.next.next.data, 67)

unittest.main()
