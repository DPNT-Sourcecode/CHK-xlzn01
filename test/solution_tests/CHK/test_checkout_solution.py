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

    def test_two_free_b_for_four_e(self):
        self.assertEqual(
            160,
            checkout_solution.checkout("EEEEBB")
        )

    def test_single_free_b_multibuy_b_for_two_e(self):
        self.assertEqual(
            125,
            checkout_solution.checkout("EEBBB")
        )

    def test_multibuy_a_with_three(self):
        self.assertEqual(
            130,
            checkout_solution.checkout("AAA")
        )

    def test_multibuy_a_with_five(self):
        self.assertEqual(
            200,
            checkout_solution.checkout("AAAAA")
        )

    def test_multibuy_a_and_single_with_six(self):
        self.assertEqual(
            250,
            checkout_solution.checkout("AAAAAA")
        )

    def test_checkout_single_e_returns_e(self):
        self.assertEqual(
            40,
            checkout_solution.checkout("E")
        )