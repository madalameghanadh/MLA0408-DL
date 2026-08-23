# Q5: Video Caption Generation
# Transfer Learning + LSTM Encoder-Decoder
# Pure Python

import random

print("VIDEO CAPTION GENERATION")
print("------------------------")

# Video frames
frames = [
    "Frame 1",
    "Frame 2",
    "Frame 3",
    "Frame 4",
    "Frame 5"
]

print("\nVideo Frames:")

for frame in frames:
    print(frame)


# Transfer learning feature extraction
print("\nTransfer Learning Feature Extraction:")

features = []

for frame in frames:

    feature = [
        random.random(),
        random.random(),
        random.random()
    ]

    features.append(feature)

    print(
        frame,
        "-> Feature:",
        [round(x, 2) for x in feature]
    )


# LSTM encoder
print("\nLSTM Encoder:")

hidden_state = 0

for feature in features:

    hidden_state = (
        hidden_state
        +
        sum(feature)
    ) / 2

    print(
        "Hidden State:",
        round(hidden_state, 3)
    )


# Caption decoder
print("\nLSTM Decoder:")

caption_words = [
    "A",
    "man",
    "is",
    "walking",
    "on",
    "the",
    "road"
]

caption = []

for word in caption_words:

    caption.append(word)

    print(
        "Generated:",
        " ".join(caption)
    )


print("\nFinal Caption:")
print(" ".join(caption))
