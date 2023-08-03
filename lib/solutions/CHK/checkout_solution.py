from typing import Dict, Tuple, List, Union

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
                             special_offers_to_process: Dict[str, List[Tuple[int, Union[int, str]]]]) -> Tuple[
        int, int]:
        # If no special available for item.
        if item not in special_offers_to_process:
            return 0, 0

        # Keep track of the discounts for freebees.
        freebee_discounts: int = 0

        # Keep track of the cost of items when multibuy discounts are applied.
        multibuy_cost: List[Tuple[int, float]] = []
        for offer in special_offers_to_process[item]:
            num_item_required: int
            reward: Union[int, str]
            num_item_required, reward = offer

            # If is a freebee reward: (2, "1B").
            if isinstance(reward, str):
                num_freebee_items: int = int(reward[0])
                freebee_item: str = reward[1]

                # Check if freebee item is in the basket, if not then no reward given.
                if items.get(freebee_item, 0) == 0:
                    continue

                num_times_offer_applied: int = count_of_item // num_item_required
                # Take the 'free' items out of the basket.
                items[freebee_item] -= (num_freebee_items * num_times_offer_applied)

                # Calculate the total discount.
                freebee_discounts += price_table[freebee_item] * num_freebee_items * num_times_offer_applied
            # Process multibuy offers.
            else:
                cost_of_single_item_when_using_multibuy: float = reward / num_item_required

                # Number of items available at multibuy price.
                multibuy_cost.append((num_item_required, cost_of_single_item_when_using_multibuy))

        # Calculate the best combination of multibuy offers.
        multibuy_discounts: int = 0
        # Sort the multibuy cost by the cost of a single item.
        multibuy_cost.sort(key=lambda x: x[1])

        # Keep track of the number of items that have been processed as a multibuy.
        num_items_processed: int = 0
        for num_item_required, cost_of_single_item_when_using_multibuy in multibuy_cost:
            # If we have processed all the items, then break.
            if count_of_item - num_items_processed == 0:
                break

            elif count_of_item - num_items_processed >= num_item_required:
                multibuy_discounts += cost_of_single_item_when_using_multibuy * num_item_required

                # Keep track of the number of items used so far.
                num_items_processed += num_item_required

            else:
                pass

        return num_items_processed, (freebee_discounts + multibuy_discounts)

    total_checkout_value: int = 0

    # Apply all freebees first.
    for item, count_of_item in items.items():
        _, freebee_discount = apply_special_offers(
            item=item, count_of_item=count_of_item, special_offers_to_process=freebees_specials
        )

    # Apply the special offers and calculate costs.
    for item, count_of_item in items.items():
        num_items_used, multibuy_cost = apply_special_offers(
            item=item, count_of_item=count_of_item, special_offers_to_process=multibuy_specials
        )

        remaining_items_at_cost = count_of_item - num_items_used
        total_checkout_value += multibuy_cost
        total_checkout_value += remaining_items_at_cost * price_table[item]

    return int(total_checkout_value)


if __name__ == '__main__':
    basket: str = "AAAAA"

    print(checkout(skus=basket))

