from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2

app = Flask(__name__)
model = YOLO('model.pt')

@app.route('/', methods=['POST'])
def detect_video():
    data = request.get_json()
    if not data or 'videoUrl' not in data:
        return jsonify({'error': 'no videoUrl provided'}), 400

    cap = cv2.VideoCapture(data['videoUrl'])
    results_list = []
    frame_idx = 0

    while frame_idx < 50:
        ret, frame = cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out = model(rgb)

        frame_dets = []
        for r in out:
            for xyxy, conf, cls in zip(r.boxes.xyxy, r.boxes.conf, r.boxes.cls):
                x1, y1, x2, y2 = map(float, xyxy)
                frame_dets.append({
                    'bbox': [x1, y1, x2, y2],
                    'score': float(conf),
                    'class': int(cls)
                })
        results_list.append({'frame': frame_idx, 'detections': frame_dets})
        frame_idx += 1

    cap.release()
    return jsonify(results_list)
