import unittest
from fractions import Fraction

from my_sum import sum


class TestSum(unittest.TestCase):

    def test_sum_list_int(self):
        """
        Testing the sum function with a list of integers
        """

        list_of_int = [1, 2, 3]
        result = sum(list_of_int)

        self.assertEqual(result, 6)

    def test_sum_list_fraction(self):
        """
        Testing the sum function with a list of fractions
        """

        list_of_fractions = [Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)]
        result = sum(list_of_fractions)

        self.assertEqual(result, 1)

    def test_sum_list_floats(self):
        """
        Testing the sum function with a list of float values
        """

        list_of_floats = [1.2, 2.34, 2.001]
        result = sum(list_of_floats)

        self.assertEqual(result, 5.541)

    def test_sum_integer_should_raise_exception(self):
        """
        Testing the sum function with an integer input
        """

        with self.assertRaises(TypeError):
            sum(1)

    def test_sum_string_should_raise_exception(self):
        """
        Testing the sum function with a string input
        """

        with self.assertRaises(TypeError):
            sum('banana')

    def test_sum_list_string_should_raise_exception(self):
        """
        Testing the sum function with a string input
        """

        with self.assertRaises(TypeError):
            sum(['banana', 'apple'])


if __name__ == "__main__":
    unittest.main()
