from game_logic.game import init_game, play_round

if __name__ == "__main__":
    init_game = init_game()
    play_round(init_game["player_1"],init_game["player_2"])