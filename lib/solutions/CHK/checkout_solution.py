from typing import Dict, Tuple, NamedTuple
from collections import namedtuple

Specials = namedtuple(typename="Specials", field_names=("quantity", "price"))
MultibuySpecial = namedtuple(typename="MultibuySpecial", field_names=("item", "quantity", "price"))

stock_prices_by_sku: Dict[str, int] = {
    "A": 50, "B": 30, "C": 20, "D": 15
}

special_by_sku: Dict[str, Specials] = {
    "A": Specials(quantity=3, price=130), "B": Specials(quantity=2, price=45)
}

price_table = {
    "A": {"price": 50, "specials": {"3A": 130, "5A": 200}},
    "B": {"price": 30, "specials": {"2B": 45}},
    "C": {"price": 20},
    "D": {"price": 15},
    "E": {"price": 40, "specials": {"2E": "B"}}
}


def get_count_and_remove(skus: str, letter: str) -> Tuple[str, int]:
    count: int = skus.count(letter)
    # Replace the input value
    result = skus.replace(letter, "")
    return result, count


def find_quotient_and_remainder(dividend: int, divisor: int) -> Tuple[int, int]:
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    return quotient, remainder


def calculate_price_for_item_of_type(letter: str, count: int) -> int:
    single_price: int = stock_prices_by_sku[letter]
    # Calculate with no specials.
    if letter not in special_by_sku:
        return single_price * count

    special: Specials = special_by_sku[letter]
    num_of_specials, num_of_singles = find_quotient_and_remainder(
        dividend=count,
        divisor=special.quantity
    )

    return (num_of_specials * special.price) + (num_of_singles * single_price)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # Calculate total price without any special offers.
    total_price: int = 0
    for item in skus:
        # Invalid product inside.
        if item not in price_table:
            return -1
        total_price += price_table[item]["price"]

    for item in price_table:
        # If there is a special for the item.
        if "specials" in price_table[item]:
            for offer in price_table[item]["specials"]:
                count = skus.


    result: int = 0
    result += calculate_price_for_item_of_type(letter="A", count=num_a)
    result += calculate_price_for_item_of_type(letter="B", count=num_b)
    result += calculate_price_for_item_of_type(letter="C", count=num_c)
    result += calculate_price_for_item_of_type(letter="D", count=num_d)

    return result


