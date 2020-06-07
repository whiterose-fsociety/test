import unittest
from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        :return:
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result,6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        :return:
        """
        data = [Fraction(1,4),Fraction(1,4),Fraction(2,4)]
        result = sum(data)
        self.assertEqual(result,1)
    # def test_bad_type(self):
    #     data = [1,2,3]
    #     with self.assertRaises(TypeError):
    #         result = sum(data)
if __name__ == "__main__":
    unittest.main()