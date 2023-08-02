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


class TestCalculatePriceForSingle(unittest.TestCase):
    def test_with_single_and_no_specials(self):
        item: str = "D"
        num: int = 1
        self.assertEqual(
            checkout_solution.calculate_price_for_item_of_type(letter=item, count=num),
            checkout_solution.stock_prices_by_sku[item] * num
        )

    def test_with_single_and_specials_but_not_enough(self):
        item: str = "A"
        num: int = 1
        self.assertEqual(
            checkout_solution.calculate_price_for_item_of_type(letter=item, count=num),
            checkout_solution.stock_prices_by_sku[item] * num
        )

    def test_with_two_and_specials_but_not_enough(self):
        item: str = "A"
        num: int = 2
        self.assertEqual(
            checkout_solution.calculate_price_for_item_of_type(letter=item, count=num),
            checkout_solution.stock_prices_by_sku[item] * num
        )

    def test_with_three_and_specials_returns_special_once(self):
        item: str = "A"
        num: int = 3
        self.assertEqual(
            checkout_solution.calculate_price_for_item_of_type(letter=item, count=num),
            checkout_solution.special_by_sku[item].price
        )

    def test_with_four_and_specials_returns_special_once_and_one_single(self):
        item: str = "A"
        num: int = 4
        self.assertEqual(
            checkout_solution.calculate_price_for_item_of_type(letter=item, count=num),
            checkout_solution.special_by_sku[item].price + checkout_solution.stock_prices_by_sku[item]
        )

    def test_with_six_and_specials_returns_special_twice(self):
        item: str = "A"
        num: int = 6
        self.assertEqual(
            checkout_solution.calculate_price_for_item_of_type(letter=item, count=num),
            checkout_solution.special_by_sku[item].price * 2
        )


class TestCheckoutSolution(unittest.TestCase):
    def test_with_unmatching_item_returns_invalid(self):
        self.assertEqual(checkout_solution.checkout("X"), -1)

    def test_with_a_single_a_returns_cost_of_a(self):
        self.assertEqual(checkout_solution.checkout("A"), checkout_solution.stock_prices_by_sku["A"])

    def test_with_a_ab_returns_cost_of_a_b(self):
        self.assertEqual(
            checkout_solution.checkout("AB"),
            checkout_solution.stock_prices_by_sku["A"] + checkout_solution.stock_prices_by_sku["B"]
        )

    def test_with_a_aaab_returns_cost_of_special_a_and_b(self):
        self.assertEqual(
            checkout_solution.checkout("ABAA"),
            checkout_solution.special_by_sku["A"].price + checkout_solution.stock_prices_by_sku["B"]
        )
