from typing import Dict, Tuple, NamedTuple
from collections import namedtuple

price_table = {
    "A": {"price": 50, "specials": {"3A": 130, "5A": 200}},
    "B": {"price": 30, "specials": {"2B": 45}},
    "C": {"price": 20},
    "D": {"price": 15},
    "E": {"price": 40, "specials": {"2E": "B"}}
}


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
                # Determine then number of special items in the 'skus'.
                count: int = skus.count(item)

                # Compare against the number required for the special '3A' = 3.
                if count >= int(offer[0]):
                    # Compare against the item required.
                    if offer[-1] in skus:
                        count_free_item: int = skus.count(offer[-1])
                        num_times: int = count // int(offer[0])
                        num_times: int = min(num_times, count_free_item)
                        total_price -= num_times * price_table[offer[-1]]["price"]

                        # Remove used items from the basket.
                        for i in range(num_times):
                            skus = skus.replace(offer[-1], '', 1)

    return total_price
