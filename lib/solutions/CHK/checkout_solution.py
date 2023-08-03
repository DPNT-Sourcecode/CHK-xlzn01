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

    # Return if invalid item in basket.
    if any(item not in price_table for item in skus):
        return -1

    def apply_special_offers(item: str, count_of_item: int,
                             special_offers_to_process: Dict[str, List[Tuple[int, Union[int, str]]]]):
        # If no special available for item.
        if item not in special_offers_to_process:
            return 0

        best_discount: int = 0
        for offer in special_offers_to_process[item]:
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

                # Calculate a total discount.
                total_discount: int = num_times_offer_applied * (num_freebee_items * price_table[freebee_item])

            # Process multibuy discounts.
            else:
                num_times_offer_applied: int = count_of_item // num_item_required
                # Calculate the discount (difference between special and raw price) of offer.
                discount_from_offer: int = (price_table[item] * num_item_required) - reward
                total_discount: int = num_times_offer_applied * discount_from_offer

            best_discount = max(best_discount, total_discount)

        return best_discount

    total_checkout_value: int = 0

    total_freebees_discount: int = 0
    # Apply 'freebees' first, as this will take out from the basket.
    for item, count in items.items():
        if item not in freebees_specials:
            continue
        total_freebees_discount += apply_special_offers(
            item=item, count_of_item=count, special_offers_to_process=freebees_specials
        )

    # Process 'multibuys' and regular prices.
    for item, count in items.items():
        if item in multibuy_specials:
            # Take off any multibuy price.
            multibuy_discount: int = apply_special_offers(
                item=item, count_of_item=count, special_offers_to_process=multibuy_specials
            )
            total_checkout_value -= multibuy_discount

        # Add regular price.
        total_checkout_value += price_table[item] * count

    return total_checkout_value if total_checkout_value >= 0 else -1


if __name__ == '__main__':
    basket: str = "EEB"

    print(checkout(skus=basket))

