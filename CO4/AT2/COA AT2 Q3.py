# Q3: Bidirectional RNN
# Encoder-Decoder Translation
# Pure Python

sentence = [
    "I",
    "am",
    "going",
    "home"
]

print("BIDIRECTIONAL RNN ENCODER-DECODER")
print("--------------------------------")

print("\nInput Sentence:")
print(" ".join(sentence))

# Forward processing
forward = []

print("\nForward RNN:")

for word in sentence:

    forward.append(word)

    print(
        "Processed:",
        word
    )

# Backward processing
backward = []

print("\nBackward RNN:")

for word in reversed(sentence):

    backward.append(word)

    print(
        "Processed:",
        word
    )

# Context
print("\nCombined Context:")

for i in range(len(sentence)):

    print(
        sentence[i],
        "-> Forward:",
        forward[i],
        "| Backward:",
        backward[
            len(sentence) - 1 - i
        ]
    )

# Simple simulated translation
translation = [
    "Je",
    "vais",
    "à",
    "la",
    "maison"
]

print("\nTranslated Sentence:")
print(" ".join(translation))

print("\nBidirectional processing uses")
print("information from both directions.")
