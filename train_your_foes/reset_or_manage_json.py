import numpy as np
import json

input_easy = np.zeros(6) # 3 moves of each, alternate
input_medium = np.zeros(16) # 8 moves of each, alternate
input_hard = np.zeros(44) # 15 moves of each, alternate, next 10 cells represent avg cumulative runs at the next 5 balls by each player, alternate, followed by game history data, 3 cells, avg runs when computer won, lost, drew, and the last cell being, no of balls left

weights_0to1_easy_bats = np.ones((6,16))
weights_1to2_easy_bats = np.ones((16,8))
weights_2to3_easy_bats = np.ones((8,4))
weights_0to1_medium_bats = np.ones((16,32))
weights_1to2_medium_bats = np.ones((32,16))
weights_2to3_medium_bats = np.ones((16,5))
weights_0to1_hard_bats = np.ones((44,64))
weights_1to2_hard_bats = np.ones((64,32))
weights_2to3_hard_bats = np.ones((32,16))
weights_3to4_hard_bats = np.ones((16,7))

bias_0to1_easy_bats = np.zeros(16)
bias_1to2_easy_bats = np.zeros(8)
bias_2to3_easy_bats = np.zeros(4)
bias_0to1_medium_bats = np.zeros(32)
bias_1to2_medium_bats = np.zeros(16)
bias_2to3_medium_bats = np.zeros(5)
bias_0to1_hard_bats = np.zeros(64)
bias_1to2_hard_bats = np.zeros(32)
bias_2to3_hard_bats = np.zeros(16)
bias_3to4_hard_bats = np.zeros(7)

# Define your weights and biases
weights_biases_easy_bats = {
    "weights_0to1_easy_bats" : weights_0to1_easy_bats.tolist(),
    "weights_1to2_easy_bats" : weights_1to2_easy_bats.tolist(),
    "weights_2to3_easy_bats" : weights_2to3_easy_bats.tolist(),
    "bias_0to1_easy_bats" : bias_0to1_easy_bats.tolist(),
    "bias_1to2_easy_bats" : bias_1to2_easy_bats.tolist(),
    "bias_2to3_easy_bats" : bias_2to3_easy_bats.tolist()
}

weights_biases_medium_bats = {
    "weights_0to1_medium_bats": weights_0to1_medium_bats.tolist(),
    "weights_1to2_medium_bats": weights_1to2_medium_bats.tolist(),
    "weights_2to3_medium_bats": weights_2to3_medium_bats.tolist(),
    "bias_0to1_medium_bats": bias_0to1_medium_bats.tolist(),
    "bias_1to2_medium_bats": bias_1to2_medium_bats.tolist(),
    "bias_2to3_medium_bats": bias_2to3_medium_bats.tolist()
}

weights_biases_hard_bats = {
    "weights_0to1_hard_bats": weights_0to1_hard_bats.tolist(),
    "weights_1to2_hard_bats": weights_1to2_hard_bats.tolist(),
    "weights_2to3_hard_bats": weights_2to3_hard_bats.tolist(),
    "weights_3to4_hard_bats": weights_3to4_hard_bats.tolist(),
    "bias_0to1_hard_bats": bias_0to1_hard_bats.tolist(),
    "bias_1to2_hard_bats": bias_1to2_hard_bats.tolist(),
    "bias_2to3_hard_bats": bias_2to3_hard_bats.tolist(),
    "bias_3to4_hard_bats": bias_3to4_hard_bats.tolist()
}

weights_0to1_easy_bowls = np.ones((6,16))
weights_1to2_easy_bowls = np.ones((16,8))
weights_2to3_easy_bowls = np.ones((8,4))
weights_0to1_medium_bowls = np.ones((16,32))
weights_1to2_medium_bowls = np.ones((32,16))
weights_2to3_medium_bowls = np.ones((16,5))
weights_0to1_hard_bowls = np.ones((44,64))
weights_1to2_hard_bowls = np.ones((64,32))
weights_2to3_hard_bowls = np.ones((32,16))
weights_3to4_hard_bowls = np.ones((16,7))

bias_0to1_easy_bowls = np.zeros(16)
bias_1to2_easy_bowls = np.zeros(8)
bias_2to3_easy_bowls = np.zeros(4)
bias_0to1_medium_bowls = np.zeros(32)
bias_1to2_medium_bowls = np.zeros(16)
bias_2to3_medium_bowls = np.zeros(5)
bias_0to1_hard_bowls = np.zeros(64)
bias_1to2_hard_bowls = np.zeros(32)
bias_2to3_hard_bowls = np.zeros(16)
bias_3to4_hard_bowls = np.zeros(7)

# Define your weights and biases
weights_biases_easy_bowls = {
    "weights_0to1_easy_bowls" : weights_0to1_easy_bowls.tolist(),
    "weights_1to2_easy_bowls" : weights_1to2_easy_bowls.tolist(),
    "weights_2to3_easy_bowls" : weights_2to3_easy_bowls.tolist(),
    "bias_0to1_easy_bowls" : bias_0to1_easy_bowls.tolist(),
    "bias_1to2_easy_bowls" : bias_1to2_easy_bowls.tolist(),
    "bias_2to3_easy_bowls" : bias_2to3_easy_bowls.tolist()
}

weights_biases_medium_bowls = {
    "weights_0to1_medium_bowls": weights_0to1_medium_bowls.tolist(),
    "weights_1to2_medium_bowls": weights_1to2_medium_bowls.tolist(),
    "weights_2to3_medium_bowls": weights_2to3_medium_bowls.tolist(),
    "bias_0to1_medium_bowls": bias_0to1_medium_bowls.tolist(),
    "bias_1to2_medium_bowls": bias_1to2_medium_bowls.tolist(),
    "bias_2to3_medium_bowls": bias_2to3_medium_bowls.tolist()
}

weights_biases_hard_bowls = {
    "weights_0to1_hard_bowls": weights_0to1_hard_bowls.tolist(),
    "weights_1to2_hard_bowls": weights_1to2_hard_bowls.tolist(),
    "weights_2to3_hard_bowls": weights_2to3_hard_bowls.tolist(),
    "weights_3to4_hard_bowls": weights_3to4_hard_bowls.tolist(),
    "bias_0to1_hard_bowls": bias_0to1_hard_bowls.tolist(),
    "bias_1to2_hard_bowls": bias_1to2_hard_bowls.tolist(),
    "bias_2to3_hard_bowls": bias_2to3_hard_bowls.tolist(),
    "bias_3to4_hard_bowls": bias_3to4_hard_bowls.tolist()
}

# Save to JSON
# with open("model_weights_easy_bats.json", "w") as f:
#     json.dump(weights_biases_easy_bats, f, indent=4)
# with open("model_weights_medium_bats.json", "w") as f:
#     json.dump(weights_biases_medium_bats, f, indent=4)
# with open("model_weights_hard_bats.json", "w") as f:
#     json.dump(weights_biases_hard_bats, f, indent=4)
# with open("model_weights_easy_bowls.json", "w") as f:
#     json.dump(weights_biases_easy_bowls, f, indent=4)
# with open("model_weights_medium_bowls.json", "w") as f:
#     json.dump(weights_biases_medium_bowls, f, indent=4)
# with open("model_weights_hard_bowls.json", "w") as f:
#     json.dump(weights_biases_hard_bowls, f, indent=4)

runs_easy = (1, 2, 4, 6)
runs_medium = (0, 1, 2, 4, 6)
runs_hard = (0, 1, 2, 3, 4, 5, 6)

# score_data ((())) i = no of overs (2, 5, 10, 15, 20); j = computer, human; k = w,d,l for first 6
# for cumulative average, we go over type by over type
template = np.zeros((5, 2, 3))
score_data = {
    "no_of_matches" : {
        "easy" : {
            2 : 0,
            5 : 0,
            10 : 0,
            15 : 0,
            20 : 0
        },
        "medium" : {
            2 : 0,
            5 : 0,
            10 : 0,
            15 : 0,
            20 : 0
        },
        "hard" : {
            2 : 0,
            5 : 0,
            10 : 0,
            15 : 0,
            20 : 0
        }
    },
    "easy_overall": template.copy().tolist(),
    "easy_late_focused": template.copy().tolist(),
    "medium_overall": template.copy().tolist(),
    "medium_late_focused": template.copy().tolist(),
    "hard_overall": template.copy().tolist(),
    "hard_late_focused": template.copy().tolist(),
    "cumulative_average_per_ball_overall_2_overs" : np.zeros(12).tolist(),
    "cumulative_average_per_ball_overall_5_overs" : np.zeros(30).tolist(),
    "cumulative_average_per_ball_overall_10_overs" : np.zeros(60).tolist(),
    "cumulative_average_per_ball_overall_15_overs" : np.zeros(90).tolist(),
    "cumulative_average_per_ball_overall_20_overs" : np.zeros(120).tolist(),
    "late_focused_cumulative_average_per_ball_overall_2_overs" : np.zeros(12).tolist(),
    "late_focused_cumulative_average_per_ball_overall_5_overs" : np.zeros(30).tolist(),
    "late_focused_cumulative_average_per_ball_overall_10_overs" : np.zeros(60).tolist(),
    "late_focused_cumulative_average_per_ball_overall_15_overs" : np.zeros(90).tolist(),
    "late_focused_cumulative_average_per_ball_overall_20_overs" : np.zeros(120).tolist()
}

# with open("score_data.json", 'w') as sd:
#     json.dump(score_data, sd, indent=4)

# now, we define average as the normal sum of scores upon no of matches
# but, late focused average isn't (a + b + c) / 3, it is ((a + b) / 2 + c) / 2
# let's do some math
# let average = late focused average
# multiply both sides by 12
# we get 4a + 4b + 4c = 3a + 3b + 6c
# clearly, in late focused average, the newer scores have more weightage
# this shows whether the user is improving or not, on a more instantaneous scale, while not ignoring the early scores
# what i mean by this is, if we really want instantaneous changes, we can do (last match + second last match) / 2, but that doesnt consider the previous scores
# also late focused average is easy to calculate since the late focused average of previous match is already in the array, we just need to do (this match + last match) divided by 2 
