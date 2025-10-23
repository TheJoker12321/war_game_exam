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
    pass

