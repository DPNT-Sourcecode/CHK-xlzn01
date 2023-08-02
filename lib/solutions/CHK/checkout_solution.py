from typing import Dict, Tuple, NamedTuple
from collections import namedtuple

Specials = namedtuple(typename="Specials", field_names=("quantity", "price"))

stock_prices_by_sku: Dict[str, int] = {
    "A": 50, "B": 30, "C": 20, "D": 15
}

special_by_sku: Dict[str, Specials] = {
    "A": Specials(quantity=3, price=130), "B": Specials(quantity=2, price=45)
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
    result: int = -1

    # Get the count of all the products.
    skus, num_a = get_count_and_remove(skus=skus, letter="A")
    skus, num_b = get_count_and_remove(skus=skus, letter="B")
    skus, num_c = get_count_and_remove(skus=skus, letter="C")
    skus, num_d = get_count_and_remove(skus=skus, letter="D")

    # Invalid product inside.
    if len(skus) > 0:
        return -1

    return result




