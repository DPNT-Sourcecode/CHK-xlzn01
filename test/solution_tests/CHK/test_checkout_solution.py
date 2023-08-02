import unittest

from lib.solutions.CHK import checkout_solution


class TestGetCountAndRemove(unittest.TestCase):
    def test_with_no_values_returns_zero_and_empty_string(self):
        ins, count = checkout_solution.get_count_and_remove("", "a")
        self.assertEqual(ins, "")
        self.assertEqual(count, 0)

    def test_with_no_matching_values_returns_zero_and_original_string(self):
        ins, count = checkout_solution.get_count_and_remove("a", "b")
        self.assertEqual(ins, "a")
        self.assertEqual(count, 0)

    def test_with_matching_values_returns_one_and_empty_string(self):
        ins, count = checkout_solution.get_count_and_remove("a", "a")
        self.assertEqual(ins, "")
        self.assertEqual(count, 1)

    def test_with_matching_values_returns_one_and_remaining_string(self):
        ins, count = checkout_solution.get_count_and_remove("ab", "a")
        self.assertEqual(ins, "b")
        self.assertEqual(count, 1)

class TestCheckoutSolution(unittest.TestCase):
    def test_initial(self):
        pass

