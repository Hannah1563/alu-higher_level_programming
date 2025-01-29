#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 50, 30, 20]), 50)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -50, -30, -20]), -10)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([0, -1, 2, -3, 1]), 2)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7]), -7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_duplicates(self):
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.8, 3.3, 2.9]), 3.3)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == "__main__":
    unittest.main()

