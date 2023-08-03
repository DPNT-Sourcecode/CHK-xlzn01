from typing import Dict, Tuple, NamedTuple
from collections import namedtuple

price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

multibuy_specials = {
    "A": [(3, 130), (5, 200)],
    "B": [(2, 45)]
}

freebees_specials = {
    "E": [(2, "1B")]
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # Initialise the items into a dictionary with counts.
    items: Dict[str, int] = {item: skus.count(item) for item in skus}
    print(items)

    return -1


if __name__ == '__main__':
    basket: str = "AABB"

    print(checkout(skus=basket))
