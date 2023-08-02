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


class TestCheckoutSolution(unittest.TestCase):
    def test_initial(self):
        pass


