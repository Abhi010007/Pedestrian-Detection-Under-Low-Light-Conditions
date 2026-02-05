import cv2
import pandas as pd
import os
from ultralytics import YOLO  # Import YOLO from ultralytics package

# Load the YOLOv8 model (your trained model)
model = YOLO("C:/Master_Project/runs/detect/train4/weights/best.pt")  # Replace with your model path

# Directory containing all video files
video_directory = 'C:/Master_Project/High_Beam_Vids'  # Replace with your folder path
video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.avi'))]  # Add any other video extensions you need

# List to store results
results = []

# Loop through each video file in the directory
for video_file in video_files:
    video_path = os.path.join(video_directory, video_file)
    cap = cv2.VideoCapture(video_path)

    # Process the video frame by frame
    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_number += 1
        # Run inference on the frame
        results_frame = model(frame)
        
        # Extract confidence scores and associated bounding boxes
        for result in results_frame:
            for box in result.boxes:
                confidence = box.conf  # Confidence score of the detection
                class_name = model.names[int(box.cls)]  # Class name corresponding to the detection
                x1, y1, x2, y2 = box.xyxy[0].tolist()  # Bounding box coordinates (x1, y1, x2, y2)
                
                # Append the results (video name, frame number, class name, confidence score, bounding box coordinates)
                results.append([video_file, frame_number, class_name, confidence.item(), x1, y1, x2, y2])

    # Release video capture for the current video
    cap.release()

# Save results to a CSV file
df = pd.DataFrame(results, columns=['Video Name', 'Frame Number', 'Class Name', 'Confidence', 'X1', 'Y1', 'X2', 'Y2'])
df.to_csv('confidence_and_bboxes_multiple_videos.csv', index=False)

print("Confidence scores and bounding boxes for all videos saved to 'confidence_and_bboxes_multiple_videos.csv'")
