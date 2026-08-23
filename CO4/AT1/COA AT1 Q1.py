# Q1 - Transfer Learning for Plant Disease Detection
# Simple Python demonstration without TensorFlow

print("=" * 55)
print("PLANT DISEASE DETECTION USING TRANSFER LEARNING")
print("=" * 55)

# Pre-trained CNN
pretrained_model = "MobileNetV2"

print("\nPre-trained Model:", pretrained_model)

# Input image
image = "Plant_Leaf_Image.jpg"
print("Input Image:", image)

# Image preprocessing
print("\n1. Image Preprocessing")
print("   - Resize image to 224 x 224")
print("   - Normalize pixel values")

# Transfer learning
print("\n2. Transfer Learning")
print("   - Load ImageNet pre-trained weights")
print("   - Freeze early convolutional layers")
print("   - Fine-tune last 20 layers")

# Feature extraction
print("\n3. Feature Extraction")
print("   - Edges")
print("   - Textures")
print("   - Leaf patterns")
print("   - Disease symptoms")

# Data augmentation
print("\n4. Data Augmentation")
print("   - Rotation")
print("   - Horizontal Flip")
print("   - Zoom")
print("   - Brightness adjustment")
print("   - Width/Height shift")

# Classification
diseases = [
    "Healthy",
    "Bacterial Disease",
    "Fungal Disease",
    "Viral Disease",
    "Leaf Spot"
]

print("\n5. Disease Classes")
for i, disease in enumerate(diseases, 1):
    print(i, "-", disease)

# Simulated prediction
predicted_disease = "Leaf Spot"

print("\n6. Prediction")
print("Predicted Disease:", predicted_disease)

print("\n" + "=" * 55)
print("TRANSFER LEARNING MODEL COMPLETED")
print("=" * 55)
