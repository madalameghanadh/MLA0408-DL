# Q2 - DenseNet and PixelNet
# Semantic Image Segmentation for Autonomous Driving

print("=" * 60)
print("DENSENET + PIXELNET SEMANTIC IMAGE SEGMENTATION")
print("=" * 60)

# Input image
image = "road_image.jpg"

print("\nInput Image:", image)

# DenseNet feature extraction
print("\n1. DenseNet Feature Extraction")
print("   - Extract low-level features")
print("   - Extract high-level features")
print("   - Reuse features using dense connections")
print("   - Improve gradient flow")

# Dense connectivity
print("\n2. Dense Connectivity")
print("   Layer 1 -> Layer 2")
print("   Layer 1 -> Layer 3")
print("   Layer 2 -> Layer 3")
print("   Layer 1 -> Layer 4")
print("   Layer 2 -> Layer 4")
print("   Layer 3 -> Layer 4")

# PixelNet
print("\n3. PixelNet Pixel-wise Prediction")
print("   - Analyze every pixel")
print("   - Assign a class to every pixel")

# Semantic classes
classes = [
    "Road",
    "Car",
    "Pedestrian",
    "Traffic Sign",
    "Building",
    "Vegetation",
    "Sky"
]

print("\n4. Semantic Classes")

for i, class_name in enumerate(classes, 1):
    print(i, "-", class_name)

# Segmentation process
print("\n5. Segmentation Process")
print("   Input Image")
print("       ↓")
print("   DenseNet")
print("       ↓")
print("   Feature Extraction")
print("       ↓")
print("   Dense Connectivity")
print("       ↓")
print("   PixelNet")
print("       ↓")
print("   Pixel-wise Classification")
print("       ↓")
print("   Segmentation Map")

# Example pixel predictions
print("\n6. Example Pixel Predictions")

pixels = {
    "(10,10)": "Sky",
    "(50,80)": "Building",
    "(120,100)": "Car",
    "(180,120)": "Road",
    "(150,200)": "Pedestrian"
}

for pixel, prediction in pixels.items():
    print("Pixel", pixel, "->", prediction)

print("\n7. Accuracy Improvement")
print("   DenseNet : Feature reuse and better gradient flow")
print("   PixelNet : Pixel-level classification")
print("   Combined : Detailed and accurate segmentation")

print("\n" + "=" * 60)
print("SEMANTIC SEGMENTATION COMPLETED")
print("=" * 60)
