import random
def create_card(rank:str,suite:str) -> dict:
    cards_values = {"2": 2, "3": 3,"4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    type_suites = ["H", "C", "D","S"]
    if suite not in type_suites:
        raise ValueError
    card_dictionary = {"rank": rank, "suite": suite, "value":cards_values[rank]}
    return card_dictionary

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    return "WAR"

def create_deck() -> list[dict]:
    list_card_deck = []
    type__suites = ["H", "C", "D","S"]
    type_special_cards = ["J", "Q", "K", "A"]
    for i in range(2, 11):
        for j in type__suites:
            list_card_deck.append(create_card(str(i),j))
    for i in type_special_cards:
        for j in type__suites:
            list_card_deck.append(create_card(i, j))
    return list_card_deck


def shuffle(deck:list[dict]) -> list[dict]:
    new_shuffle_deck = deck[:]
    for i in range(1000):
        index_1 = random.randrange(0, 52)
        index_2 = random.randrange(0, 52)
        if index_1 == index_2:
            while index_1 == index_2:
                index_1 = random.randrange(0, 52)
                index_2 = random.randrange(0, 52)
        new_shuffle_deck[index_1], new_shuffle_deck[index_2] = new_shuffle_deck[index_2],new_shuffle_deck[index_1]
    return new_shuffle_deck

