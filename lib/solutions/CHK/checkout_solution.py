from typing import Dict, Tuple, NamedTuple, List, Union
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

    def apply_special_offers(item: str, count_of_item: int,
                             special_offers_to_process: Dict[str, List[Tuple[int, Union[int, str]]]]):
        # If no special available for item.
        if item not in special_offers_to_process:
            return 0

        best_discount: int = 0
        for offer in special_offers_to_process:
            num_item_required: int
            offer: Tuple[int, Union[int, str]]
            num_item_required, reward = offer

            # If is a 'freebee' reward: (2, "1B").
            if isinstance(reward, str):
                num_freebee_items: int = int(reward[0])
                freebee_item: str = reward[1]

                # Check if freebee item is in the basket, if not then no reward.
                if items.get(freebee_item) == 0:
                    continue

                num_times_offer_applied: int = count_of_item // num_item_required
                # Take the 'free' items out of the basket.
                items[freebee_item] -= (num_freebee_items * num_times_offer_applied)


    return -1


if __name__ == '__main__':
    basket: str = "AABB"

    print(checkout(skus=basket))

