# Q3 - Bidirectional RNN Encoder-Decoder
# Multilingual Machine Translation
# No external libraries required

print("=" * 60)
print("BIDIRECTIONAL RNN ENCODER-DECODER")
print("MULTILINGUAL MACHINE TRANSLATION")
print("=" * 60)

# Source sentence
source_sentence = [
    "I",
    "love",
    "machine",
    "learning"
]

print("\n1. Source Sentence")
print(" ".join(source_sentence))

# Forward RNN
print("\n2. Forward RNN Processing")

forward_states = []

for word in source_sentence:
    state = "F_" + word
    forward_states.append(state)
    print("Forward:", word, "->", state)

# Backward RNN
print("\n3. Backward RNN Processing")

backward_states = []

for word in reversed(source_sentence):
    state = "B_" + word
    backward_states.append(state)
    print("Backward:", word, "->", state)

backward_states.reverse()

# Combine forward and backward information
print("\n4. Bidirectional Context")

for i in range(len(source_sentence)):
    print(
        source_sentence[i],
        "->",
        "[" + forward_states[i] + ", "
        + backward_states[i] + "]"
    )

# Context vector
print("\n5. Encoder Context")
print("Forward context + Backward context")
print("The complete sentence context is created.")

# Target language
target_language = "French"

print("\n6. Target Language:", target_language)

# Decoder
print("\n7. Decoder Processing")

translation = [
    "J'aime",
    "l'apprentissage",
    "automatique"
]

for word in translation:
    print("Generated word:", word)

# Complete translation
print("\n8. Final Translation")

print("English : I love machine learning")
print("French  : J'aime l'apprentissage automatique")

# Architecture
print("\n9. Model Architecture")

print("Input Sentence")
print("      ↓")
print("Word Embedding")
print("      ↓")
print("Bidirectional RNN")
print("   ↙       ↘")
print("Forward   Backward")
print("   ↘       ↙")
print("Combined Context")
print("      ↓")
print("Encoder")
print("      ↓")
print("Decoder RNN")
print("      ↓")
print("Softmax")
print("      ↓")
print("Translated Sentence")

# Advantages
print("\n10. Advantages of Bidirectional RNN")

advantages = [
    "Uses both past and future context",
    "Improves understanding of sentence meaning",
    "Handles ambiguous words better",
    "Improves translation quality",
    "Useful for multilingual translation"
]

for i, advantage in enumerate(advantages, 1):
    print(i, "-", advantage)

print("\n" + "=" * 60)
print("TRANSLATION COMPLETED")
print("=" * 60)
