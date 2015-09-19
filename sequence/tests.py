from django.test import TestCase
from sequence.generator import fibonacci_n


class FibonacciTest(TestCase):

    def test_negative_number(self):
        """
        Calling fibonacci at a negative number should raise an index error.
        """
        with self.assertRaises(IndexError):
            fibonacci_n(-2)

    def test_zero_length(self):
        """
        Calling fibonacci(0) should return an empty list.
        """
        self.assertListEqual(list(fibonacci_n(0)), [])

    def test_positive_numbers(self):
        """
        Calling fibonacci with a positive number should return a
        """
        self.assertListEqual(list(fibonacci_n(5)), [0, 1, 1, 2, 3])
        self.assertListEqual(list(fibonacci_n(8)), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_not_a_number(self):
        with self.assertRaises(TypeError):
            fibonacci_n("EMC Cloud Services")
