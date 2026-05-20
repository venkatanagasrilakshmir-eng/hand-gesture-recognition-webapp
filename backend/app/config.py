import os

class Config:
    MODEL_PATH = os.environ.get('MODEL_PATH', 'models/hand_gesture_model.h5')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    CORS_ORIGINS = '*'
