# Q1: Transfer Learning
# Skin Cancer Detection
# Pure Python - No TensorFlow / PyTorch

import random

# Simulated pre-trained CNN layers
layers = [
    "Conv1",
    "Conv2",
    "Conv3",
    "Conv4",
    "Conv5",
    "Fully Connected"
]

# Freeze early layers
frozen_layers = [
    "Conv1",
    "Conv2",
    "Conv3",
    "Conv4"
]

# Fine-tune later layers
fine_tuned_layers = [
    "Conv5",
    "Fully Connected"
]

print("TRANSFER LEARNING - SKIN CANCER DETECTION")
print("------------------------------------------")

print("\nPre-trained CNN Layers:")

for layer in layers:
    print(layer)

print("\nFrozen Layers:")

for layer in frozen_layers:
    print(layer)

print("\nFine-tuned Layers:")

for layer in fine_tuned_layers:
    print(layer)

# Simulated classification
classes = ["Benign", "Malignant"]

prediction = random.choice(classes)

print("\nInput: Dermoscopic Skin Image")
print("Predicted Class:", prediction)

print("\nTransfer learning allows the model")
print("to reuse previously learned image features.")
