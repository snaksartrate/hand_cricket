import numpy as np
import functions_mode_easy
import sys

toss_winner, toss_winners_choice = functions_mode_easy.toss()
no_of_overs = int(sys.argv[1])

input = np.zeros(7) # 5 moves of computer, 2 of human