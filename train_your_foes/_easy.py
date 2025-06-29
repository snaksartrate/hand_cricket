import numpy as np
import functions_easy
import sys

toss_winner, toss_winners_choice = functions_easy.toss()
no_of_overs = int(sys.argv[1])

input = np.zeros(6) # 3 of each player, alternate, latest first, computer even, human odd indices