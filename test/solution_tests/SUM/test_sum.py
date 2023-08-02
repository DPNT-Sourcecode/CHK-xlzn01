import unittest

from lib.solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    def test_sum_with_one_and_two_equals_three(self):
        self.assertEquals(sum_solution.compute(1, 2), 3)

    def test_sum_with_two_and_three_equals_five(self):
        self.assertEquals(sum_solution.compute(2, 3), 5)

    def test_sum_with_zero_and_one_returns_one(self):
        self.assertEquals(sum_solution.compute(0, 1), 1)

    def test_sum_with_five_and_six_returns_eleven(self):
        self.assertEquals(sum_solution.compute(5, 6), 11)


