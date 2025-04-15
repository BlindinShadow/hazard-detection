from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
import numpy as np

app = Flask(__name__)
model = YOLO('weights.pt')  # load your weights

@app.route('/', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'no image provided'}), 400

    img = Image.open(request.files['image'].stream).convert('RGB')
    results = model(img)

    detections = []
    for r in results:
        for xyxy, conf, cls in zip(r.boxes.xyxy, r.boxes.conf, r.boxes.cls):
            x1, y1, x2, y2 = map(float, xyxy)
            detections.append({
                'bbox': [x1, y1, x2, y2],
                'score': float(conf),
                'class': int(cls)
            })
    return jsonify(detections)
