import numpy as np
import json

weights_0to1_easy = np.ones((7,16))
weights_1to2_easy = np.ones((16,8))

bias_0to1_easy = np.zeros(16)
bias_1to2_easy = np.zeros(8)

weights_biases = {
    "weights_0to1_easy": weights_0to1_easy.tolist(),
    "weights_1to2_easy": weights_1to2_easy.tolist(),
    "bias_0to1_easy": bias_0to1_easy.tolist(),
    "bias_1to2_easy": bias_1to2_easy.tolist(),
}

with open("weights_easy.json", "w") as f:
    json.dump(weights_biases, f, indent=4)

# def load_model_weights(filename):
#     with open(filename, "r") as f:
#         data = json.load(f)
#     return {key: np.array(val) for key, val in data.items()}
