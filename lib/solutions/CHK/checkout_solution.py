from typing import Dict, Tuple, NamedTuple
from collections import namedtuple

Specials = namedtuple(typename="Specials", field_names=("quantity", "price"))

stock_prices_by_sku: Dict[str, int] = {
    "A": 50, "B": 30, "C": 20, "D": 15
}

special_by_sku: Dict[str, Tuple[int, int]] = {
    "A": Specials(quantity=3, price=130), "B": Specials(quantity=2, price=45)
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    result: int = -1
    num_a = skus.count("a")

    return result

