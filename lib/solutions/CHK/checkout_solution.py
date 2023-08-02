from typing import Dict, Tuple, NamedTuple
from collections import namedtuple

Specials = namedtuple(typename="Specials", field_names=("quantity", "price"))

stock_prices_by_sku: Dict[str, int] = {
    "A": 50, "B": 30, "C": 20, "D": 15
}

special_by_sku: Dict[str, Tuple[int, int]] = {
    "A": Specials(quantity=3, price=130), "B": Specials(quantity=2, price=45)
}


def get_count_and_remove(skus: str, letter: str) -> Tuple[str, int]:
    count: int = skus.count(letter)
    # Replace the input value
    result = skus.replace(letter, "")
    return result, count


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    result: int = -1
    skus, num_a = get_count_and_remove(skus=skus, letter="a")
    skus, num_b = get_count_and_remove(skus=skus, letter="b")
    skus, num_c = get_count_and_remove(skus=skus, letter="c")
    skus, num_d = get_count_and_remove(skus=skus, letter="d")

    return result

