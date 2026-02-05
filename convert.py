import os
import random
import shutil

# Paths
src_train_img_dir = "C:/Master_Project/train/train/train_images"  # Directory with images
src_train_labels_dir = "C:/Master_Project/train/train_labels"  # Directory with YOLO labels
train_img_dir = "C:/Master_Project/training/images"  # Destination directory for training images
train_label_dir = "C:/Master_Project/training/labels"  # Destination directory for training labels
val_img_dir = "C:/Master_Project/val/images"  # Destination directory for validation images
val_label_dir = "C:/Master_Project/val/labels"  # Destination directory for validation labels

# Ensure the destination directories exist
os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Function to split dataset into train and validation
def split_dataset(img_dir, label_dir, train_img_dir, train_label_dir, val_img_dir, val_label_dir, split_ratio=0.8):
    # Get all image filenames (without extensions)
    image_files = [f for f in os.listdir(img_dir) if f.endswith('.jpg')]  # Adjust if images are not .jpg
    
    # Shuffle the image files randomly
    random.shuffle(image_files)
    
    # Calculate the number of training images
    train_size = int(len(image_files) * split_ratio)
    
    # Split into train and validation sets
    train_files = image_files[:train_size]
    val_files = image_files[train_size:]
    
    # Move the files to the respective folders
    for file in train_files:
        img_path = os.path.join(img_dir, file)
        label_path = os.path.join(label_dir, file.replace('.jpg', '.txt'))  # Change extension to .txt
        
        # Move image and label to train directories
        shutil.move(img_path, os.path.join(train_img_dir, file))
        shutil.move(label_path, os.path.join(train_label_dir, file.replace('.jpg', '.txt')))
        
    for file in val_files:
        img_path = os.path.join(img_dir, file)
        label_path = os.path.join(label_dir, file.replace('.jpg', '.txt'))
        
        # Move image and label to val directories
        shutil.move(img_path, os.path.join(val_img_dir, file))
        shutil.move(label_path, os.path.join(val_label_dir, file.replace('.jpg', '.txt')))
    
    print(f"Dataset split: {len(train_files)} training images and {len(val_files)} validation images.")

# Call the function to split the dataset
split_dataset(src_train_img_dir, src_train_labels_dir, train_img_dir, train_label_dir, val_img_dir, val_label_dir, split_ratio=0.8)
