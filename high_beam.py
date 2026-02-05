from ultralytics import YOLO
import cv2
import os

# Load your trained model
model = YOLO('runs/detect/train4/weights/best.pt')

# Folder with video clips
video_folder = 'High_Beam_Vids'
output_folder = 'high_beam_results'
os.makedirs(output_folder, exist_ok=True)

# Target class (0 = person by default if trained that way)
target_class_id = 0

# Loop through videos
for video_name in os.listdir(video_folder):
    if video_name.endswith('.mp4'):
        video_path = os.path.join(video_folder, video_name)
        results = model(video_path, stream=True)

        confidences = []

        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                if cls == target_class_id:
                    confidences.append(conf)

        avg_conf = sum(confidences) / len(confidences) if confidences else 0.0

        print(f"[{video_name}] Average pedestrian confidence: {avg_conf:.3f}")

        # Save inference video with bounding boxes
        save_path = os.path.join(output_folder, f"det_{video_name}")
        model.predict(video_path, save=True, project=output_folder, name=f"det_{video_name.split('.')[0]}")
