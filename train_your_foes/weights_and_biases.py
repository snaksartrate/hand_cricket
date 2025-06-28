import numpy as np
import json

input_easy = np.zeros(7) # 5 moves of computer, 2 of human
input_medium = np.zeros(16) # 8 moves of each, alternate
input_hard = np.zeros(44) # 15 moves of each, alternate, next 10 cells represent avg cumulative runs at the next 5 balls by each player, alternate, followed by game history data, 3 cells, avg runs when computer won, lost, drew, and the last cell being, no of balls left

weights_0to1_easy = np.ones((7,16))
weights_1to2_easy = np.ones((16,8))
weights_0to1_medium = np.ones((16,32))
weights_1to2_medium = np.ones((32,16))
weights_0to1_hard = np.ones((44,64))
weights_1to2_hard = np.ones((64,32))
weights_2to3_hard = np.ones((32,16))

bias_0to1_easy = np.zeros(16)
bias_1to2_easy = np.zeros(8)
bias_0to1_medium = np.zeros(32)
bias_1to2_medium = np.zeros(16)
bias_0to1_hard = np.zeros(64)
bias_1to2_hard = np.zeros(32)
bias_2to3_hard = np.zeros(16)

# Define your weights and biases
weights_biases = {
    "weights_0to1_easy": weights_0to1_easy.tolist(),
    "weights_1to2_easy": weights_1to2_easy.tolist(),
    "bias_0to1_easy": bias_0to1_easy.tolist(),
    "bias_1to2_easy": bias_1to2_easy.tolist(),

    "weights_0to1_medium": weights_0to1_medium.tolist(),
    "weights_1to2_medium": weights_1to2_medium.tolist(),
    "bias_0to1_medium": bias_0to1_medium.tolist(),
    "bias_1to2_medium": bias_1to2_medium.tolist(),

    "weights_0to1_hard": weights_0to1_hard.tolist(),
    "weights_1to2_hard": weights_1to2_hard.tolist(),
    "weights_2to3_hard": weights_2to3_hard.tolist(),
    "bias_0to1_hard": bias_0to1_hard.tolist(),
    "bias_1to2_hard": bias_1to2_hard.tolist(),
    "bias_2to3_hard": bias_2to3_hard.tolist(),
}

# Save to JSON
with open("model_weights.json", "w") as f:
    json.dump(weights_biases, f, indent=4)

runs_easy = (1, 2, 4, 6)
runs_medium = (0, 1, 2, 4, 6)
runs_hard = (0, 1, 2, 3, 4, 5, 6)

def load_model_weights(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return {key: np.array(val) for key, val in data.items()}
