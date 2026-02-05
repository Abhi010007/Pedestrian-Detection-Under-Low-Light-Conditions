import os
import random
import xml.etree.ElementTree as ET
from PIL import Image

# Function to convert XML to YOLO format
def xml_to_yolo(xml_file, image_width, image_height):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    label_data = []
    
    for obj in root.findall('object'):
        # Get the class name (you can map this to an integer class ID)
        class_name = obj.find('name').text
        class_id = 0  # Update with the correct class ID mapping if you have multiple classes
        
        # Get the bounding box coordinates
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        
        # Convert to YOLO format (center_x, center_y, width, height)
        x_center = (xmin + xmax) / 2 / image_width
        y_center = (ymin + ymax) / 2 / image_height
        width = (xmax - xmin) / image_width
        height = (ymax - ymin) / image_height
        
        label_data.append(f"{class_id} {x_center} {y_center} {width} {height}")
    
    return label_data

# Paths
src_train_xml_dir = "C:/Master_Project/train/train/train_annotations"  # Directory with XML files (train)
output_train_labels_dir = "C:/Master_Project/train/train_labels"  # Output directory for YOLO label files (train)
src_train_img_dir = "C:/Master_Project/train/train/train_images"  # Directory with images (train)

# Ensure the output directory for labels exists
os.makedirs(output_train_labels_dir, exist_ok=True)

# Process training images and convert corresponding XML to YOLO format
def process_images_and_labels(src_img_dir, src_xml_dir, output_labels_dir):
    image_files = [f for f in os.listdir(src_img_dir) if f.endswith('.jpg')]  # Adjust if your images are not .jpg
    
    # Process images and labels
    for img_file in image_files:
        img_path = os.path.join(src_img_dir, img_file)
        img_name, _ = os.path.splitext(img_file)  # Remove file extension for XML/label file matching
        
        # Get corresponding XML file
        xml_file = os.path.join(src_xml_dir, img_name + '.xml')
        
        if os.path.exists(xml_file):
            # Get image dimensions using Pillow
            with Image.open(img_path) as img:
                img_width, img_height = img.size
            
            # Convert XML to YOLO format
            labels = xml_to_yolo(xml_file, img_width, img_height)
            
            # Write YOLO labels to a .txt file in the train_labels directory
            label_file = os.path.join(output_labels_dir, img_name + '.txt')
            with open(label_file, 'w') as f:
                for label in labels:
                    f.write(label + '\n')
            print(f"Converted: {xml_file} -> {label_file}")
        else:
            print(f"XML file not found for image: {img_file}")

# Process and convert the XML annotations to YOLO format
process_images_and_labels(src_train_img_dir, src_train_xml_dir, output_train_labels_dir)
