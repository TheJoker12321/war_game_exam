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
    pass

def shuffle(deck:list[dict]) -> list[dict]:
    pass

