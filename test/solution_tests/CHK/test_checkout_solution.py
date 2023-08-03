import unittest

from lib.solutions.CHK import checkout_solution


class TestCheckoutSolution(unittest.TestCase):
    def test_with_unmatching_item_returns_invalid(self):
        self.assertEqual(-1, checkout_solution.checkout("X"))

    def test_with_a_single_a_returns_cost_of_a(self):
        self.assertEqual(checkout_solution.price_table["A"], checkout_solution.checkout("A"))

    def test_with_a_ab_returns_cost_of_a_b(self):
        self.assertEqual(
            checkout_solution.price_table["A"] + checkout_solution.price_table["B"],
            checkout_solution.checkout("AB")
        )

    def test_with_a_aaab_returns_cost_of_special_a_and_b(self):
        self.assertEqual(
            130 + checkout_solution.price_table["B"],
            checkout_solution.checkout("ABAA")
        )

    def test_single_free_b_for_two_e(self):
        self.assertEqual(
            80,
            checkout_solution.checkout("EEB")
        )
