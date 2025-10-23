def create_player(name:str = "AI") -> dict:
    player_dictionary = {"name": name, "hand": [], "won_pile": []}
    return player_dictionary

def init_game() -> dict:
    pass

def play_round(p1:dict,p2:dict):
    pass

print(create_player("Gal"))