from flask import Blueprint, request, jsonify
from .model import predict_gesture

api = Blueprint('api', __name__)

@api.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    result = predict_gesture(request.files['file'])
    return jsonify({'prediction': result})
