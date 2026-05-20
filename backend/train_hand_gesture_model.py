import os
import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split

# 1. DATA LOADING & PREPROCESSING

# Example: Let's assume your data is in this structure:
# data/
#    ├─ Fist/
#    │    ├─ img1.png
#    │    ├─ ...
#    ├─ Open/
#    │    ├─ img100.png
#    │    ├─ ...
# etc.

DATA_DIR = "data/"  # Path to data folder (adjust as needed)
IMG_SIZE = 64
CLASS_NAMES = sorted([d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))])

def load_images(data_dir, img_size, class_names):
    images = []
    labels = []
    for idx, class_name in enumerate(class_names):
        class_dir = os.path.join(data_dir, class_name)
        for img_name in os.listdir(class_dir):
            img_path = os.path.join(class_dir, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img = cv2.resize(img, (img_size, img_size))
            images.append(img)
            labels.append(idx)
    images = np.array(images, dtype='float32') / 255.0
    images = images[..., np.newaxis]  # Shape: (N, 64, 64, 1)
    labels = np.array(labels)
    return images, labels

print("Loading images...")
X, y = load_images(DATA_DIR, IMG_SIZE, CLASS_NAMES)

# Split into train/val sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 2. MODEL DEFINITION

num_classes = len(CLASS_NAMES)
y_train_cat = to_categorical(y_train, num_classes)
y_val_cat = to_categorical(y_val, num_classes)

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 3. TRAINING

print("Training model...")
history = model.fit(
    X_train, y_train_cat,
    validation_data=(X_val, y_val_cat),
    epochs=12, batch_size=32
)

# 4. SAVE MODEL

os.makedirs("models", exist_ok=True)
model.save("models/hand_gesture_model.h5")
print("Model saved as models/hand_gesture_model.h5")

# 5. (Optional) Save class names, so backend can use same order
with open("models/class_names.txt", "w") as f:
    for name in CLASS_NAMES:
        f.write(name + "\n")
print("Also saved models/class_names.txt")
