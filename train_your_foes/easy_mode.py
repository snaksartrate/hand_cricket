import numpy as np
import json
import easy_mode_functions
import neural_networks

toss_winner, toss_winners_choice = easy_mode_functions.toss()
player_role_matrix = (('bat', 'bowl'), ('bowl', 'bat'))

weight_bias_dictionary = []

with open("weights_easy.json", 'r') as w:
    if (toss_winner == 'computer won' and toss_winners_choice == 'bat') or (toss_winner == 'human won' and toss_winners_choice == 'bowl'):
        # activate NN for computer bats
        weight_bias_dictionary = json.load(w)
    else:
        # activate NN for computer bowls
        pass

input_easy = np.zeros(7) # 5 moves of computer, 2 of human