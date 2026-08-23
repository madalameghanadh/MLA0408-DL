# Q5 - Automatic Video Caption Generation
# Transfer Learning + LSTM Encoder-Decoder

print("=" * 65)
print("AUTOMATIC VIDEO CAPTION GENERATION")
print("TRANSFER LEARNING + LSTM ENCODER-DECODER")
print("=" * 65)

# --------------------------------------------------
# 1. Input Video
# --------------------------------------------------

video = "sample_video.mp4"

print("\n1. INPUT VIDEO")
print("Video:", video)

# --------------------------------------------------
# 2. Frame Extraction
# --------------------------------------------------

print("\n2. FRAME EXTRACTION")

frames = [
    "Frame 1",
    "Frame 2",
    "Frame 3",
    "Frame 4",
    "Frame 5"
]

for frame in frames:
    print("Extracted:", frame)

# --------------------------------------------------
# 3. Transfer Learning / CNN Feature Extraction
# --------------------------------------------------

print("\n3. TRANSFER LEARNING")

pretrained_model = "VGG16"

print("Pre-trained CNN:", pretrained_model)
print("CNN weights: ImageNet")
print("Early CNN layers: Frozen")
print("CNN used as feature extractor")

print("\nExtracting visual features...")

features = [
    "Person",
    "Football",
    "Field",
    "Running",
    "Playing"
]

for feature in features:
    print("Detected feature:", feature)

# --------------------------------------------------
# 4. LSTM Encoder
# --------------------------------------------------

print("\n4. LSTM ENCODER")

print("Visual features are converted into a sequence.")
print("LSTM learns temporal information between frames.")

sequence = [
    "Person appears",
    "Person moves",
    "Person reaches football",
    "Person kicks football",
    "Person runs"
]

for step in sequence:
    print("Temporal information:", step)

# --------------------------------------------------
# 5. LSTM Decoder
# --------------------------------------------------

print("\n5. LSTM DECODER")

print("Generating caption word by word...")

caption_words = [
    "<START>",
    "A",
    "person",
    "is",
    "playing",
    "football",
    "<END>"
]

caption = ""

for word in caption_words:
    print("Predicted word:", word)

    if word not in ["<START>", "<END>"]:
        caption += word + " "

# --------------------------------------------------
# 6. Final Caption
# --------------------------------------------------

print("\n6. FINAL CAPTION")

print("Generated Caption:")
print(caption.strip() + ".")

# --------------------------------------------------
# 7. Complete Architecture
# --------------------------------------------------

print("\n7. COMPLETE ARCHITECTURE")

print("""
Video
  ↓
Frame Extraction
  ↓
Pre-trained CNN (VGG16)
  ↓
Visual Feature Extraction
  ↓
LSTM Encoder
  ↓
Temporal Representation
  ↓
LSTM Decoder
  ↓
Word Prediction
  ↓
Generated Caption
""")

# --------------------------------------------------
# 8. Role of Components
# --------------------------------------------------

print("8. ROLE OF EACH COMPONENT")

print("Transfer Learning : Extracts useful visual features")
print("CNN                : Detects objects and visual patterns")
print("LSTM Encoder       : Learns temporal information")
print("LSTM Decoder       : Generates caption words")
print("Softmax
