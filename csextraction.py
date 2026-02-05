from ultralytics import YOLO
import cv2
import os
import csv

# Load trained YOLOv8 model
model = YOLO("C:/Master_Project/runs/detect/train4/weights/best.pt")

# Folder containing videos
video_folder = "C:/Master_Project/Low_beam_Vids"
output_folder = "C:/Master_Project/output_frames"
os.makedirs(output_folder, exist_ok=True)

# CSV file to save detailed detection data
csv_output_path = "detection_details.csv"

# Create/open CSV file
with open(csv_output_path, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["video_name", "frame_number", "class_id", "confidence", "x1", "y1", "x2", "y2"])

    # Loop over each video
    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mp4"):
            video_path = os.path.join(video_folder, video_file)
            cap = cv2.VideoCapture(video_path)
            frame_count = 0

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                results = model(frame)[0]
                for box in results.boxes:
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    x1, y1, x2, y2 = [int(coord) for coord in box.xyxy[0]]

                    # Save detection info to CSV
                    writer.writerow([video_file, frame_count, cls, round(conf, 4), x1, y1, x2, y2])

                # Optional: Save annotated frames
                # Uncomment below if you want bounding boxes on saved images
                # annotated = results.plot()
                # frame_name = f"{os.path.splitext(video_file)[0]}_frame{frame_count}.jpg"
                # cv2.imwrite(os.path.join(output_folder, frame_name), annotated)

                frame_count += 1

            cap.release()

print(f"✅ Detection data saved to: {csv_output_path}")
