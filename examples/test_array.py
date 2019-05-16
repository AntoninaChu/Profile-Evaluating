from array import Array
from unittest import TestCase
import unittest

class TestArray(TestCase):
    def setUp(self):
        self.arr = Array(27)
    def test_setitem_getitem(self):
        self.arr[0] = 67
        self.arr[1] = 45
        self.arr[2] = 23
        self.arr[3] = 90
        self.arr[4] = 27
        self.assertEqual(len(self.arr), 27)
        self.assertEqual(self.arr[4], 27)
        self.assertEqual(self.arr[1], 45)
        self.assertEqual(self.arr[3], 90)
    def test_clear(self):
        self.arr[0] = 67
        self.arr[1] = 45
        self.arr[2] = 23
        self.arr[3] = 90
        self.arr[4] = 27
        self.assertEqual(len(self.arr), 27)
        self.assertEqual(self.arr[4], 27)
        self.assertEqual(self.arr[1], 45)
        self.assertEqual(self.arr[3], 90)
        self.arr.clear('clean')
        self.assertEqual(self.arr[4], 'clean')
        self.assertEqual(self.arr[1], 'clean')
        self.assertEqual(self.arr[3], 'clean')

unittest.main()
