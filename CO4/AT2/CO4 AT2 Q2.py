# Q2: DenseNet and PixelNet
# Road Scene Segmentation
# Pure Python

import random

classes = [
    "Background",
    "Road",
    "Pedestrian",
    "Vehicle",
    "Traffic Sign"
]

print("DENSENET + PIXELNET ROAD SEGMENTATION")
print("--------------------------------------")

print("\nClasses:")

for i, c in enumerate(classes):
    print(i, "=", c)

# Simulated feature reuse
features = []

print("\nDenseNet Feature Reuse:")

for layer in range(1, 6):

    feature = "Feature_" + str(layer)

    features.append(feature)

    print(
        "Layer",
        layer,
        "uses previous features:",
        features
    )

# Simulated pixel segmentation

print("\nPixel-level Classification:")

for pixel in range(10):

    predicted_class = random.choice(classes)

    print(
        "Pixel",
        pixel + 1,
        "->",
        predicted_class
    )

print("\nDenseNet improves feature reuse.")
print("PixelNet performs pixel-level classification.")
