import numpy as np
import json
import functions_medium
import sys

no_of_overs = int(sys.argv[1])

toss_winner, toss_winners_choice = functions_medium.toss()
if (toss_winner == 'computer won' and toss_winners_choice == 'bat') or (toss_winner == 'human won' and toss_winners_choice == 'bowl'):
    # call the neural net to make computer bat
    pass
else:
    # call the neural net to make computer bowl
    pass