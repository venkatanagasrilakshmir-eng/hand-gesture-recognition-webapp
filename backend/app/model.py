import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os

MODEL_PATH = os.environ.get('MODEL_PATH', 'models/hand_gesture_model.h5')
# Sample class names (replace with your dataset's classes)
CLASS_NAMES = ['Fist', 'Open', 'Okay', 'Peace', 'ThumbsUp']

model = load_model(MODEL_PATH)

def preprocess(image_file):
    img_bytes = np.frombuffer(image_file.read(), np.uint8)
    img = cv2.imdecode(img_bytes, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64)) / 255.0
    img = img.reshape(1, 64, 64, 1)
    return img

def predict_gesture(image_file):
    img = preprocess(image_file)
    pred = model.predict(img)
    idx = int(np.argmax(pred))
    return CLASS_NAMES[idx]
