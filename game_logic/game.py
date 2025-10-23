import utils.deck
def create_player(name:str = "AI") -> dict:
    player_dictionary = {"name": name, "hand": [], "won_pile": []}
    return player_dictionary

def init_game() -> dict:
    my_player = create_player("Idan")
    ai_player = create_player()
    new_deck = utils.deck.create_deck()
    new_deck_shuffled = utils.deck.shuffle(new_deck)
    for i in range(52):
        if i < 26:
            my_player["hand"].append(new_deck_shuffled[i])
        else:
            ai_player["hand"].append(new_deck_shuffled[i])
    game_dict = {"deck": new_deck_shuffled, "player_1": my_player, "player_2": ai_player}
    return game_dict


def play_round(p1:dict,p2:dict):
    while p1["hand"] and p2["hand"]:
        my_card = p1["hand"].pop(-1)
        ai_card = p2["hand"].pop(-1)
        compare = utils.deck.compare_cards(my_card, ai_card)
        if compare == "p1":
            print(f"cards of {p1["name"]}")
            p1["won_pile"].append(my_card)
            p1["won_pile"].append(ai_card)
        elif compare == "p2":
            print(f"cards of {p2["name"]}")
            p2["won_pile"].append(my_card)
            p2["won_pile"].append(ai_card)
        else:
            continue
    if len(p1["won_pile"]) > len(p2["won_pile"]):
        print(f"{p1["name"]} won!!!")
        print(f"{p1["name"]} have: {len(p1["won_pile"])} cards ")

    elif len(p2["won_pile"]) > len(p1["won_pile"]):
        print(f"{p2["name"]} won!!!")
        print(f"{p2["name"]} have: {len(p2["won_pile"])} cards ")

    else:
        print("The game ended in a draw")



