from typing import Dict, Tuple, NamedTuple
from collections import namedtuple

Specials = namedtuple(typename="Specials", field_names=("quantity", "price"))

stock_prices_by_sku: Dict[str, int] = {
    "A": 50, "B": 30, "C": 20, "D": 15
}

special_by_sku: Dict[str, Tuple[int, int]] = {
    "A": Specials(quantity=3, price=130), "B": Specials(quantity=2, price=45)
}

def get_count_and_remove(input: str, letter: str) -> int:
    count: int = input.count(letter)
    result: str = input.replace(letter)
    return result


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    result: int = -1
    num_a = skus.count("a")

    return result
