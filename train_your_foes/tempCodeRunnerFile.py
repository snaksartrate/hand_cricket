with open("model_weights_easy.json", "w") as f:
    json.dump(weights_biases_easy, f, indent=4)
with open("model_weights_medium.json", "w") as f:
    json.dump(weights_biases_medium, f, indent=4)
with open("model_weights_hard.json", "w") as f:
    json.dump(weights_biases_hard, f, indent=4)
