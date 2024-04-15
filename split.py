import os
import random
import shutil

# Set your folder path
root = "out"

folder_path = "out\images"

# Set your train and validation folder paths
train_folder = r"split\train"
valid_folder = r"split\valid"

# # Create train and validation folders if they don't exist
# os.makedirs(train_folder, exist_ok=True)
# os.makedirs(valid_folder, exist_ok=True)

# List all images in the folder
images = [f for f in os.listdir(folder_path) if f.endswith('.png')]

# Shuffle the list of images
random.shuffle(images)

# Calculate the number of images for validation
num_valid_images = int(0.1 * len(images))

# Split images into train and validation sets
train_images = images[num_valid_images:]
valid_images = images[:num_valid_images]

# Move or copy train images and labels to train folder
for image_name in train_images:
    image_path = os.path.join(root, f"images/{image_name}")
    label_path = os.path.join(root, f"labels/{image_name[:-4] + '.txt'}")  # Assuming labels have the same name with .txt extension
    shutil.copy(image_path, os.path.join(train_folder,"images"))
    shutil.copy(label_path, os.path.join(train_folder,"labels"))

# Move or copy validation images and labels to validation folder
for image_name in valid_images:
    image_path = os.path.join(root, f"images/{image_name}")
    label_path = os.path.join(root, f"labels/{image_name[:-4] + '.txt'}")  
    shutil.copy(image_path, os.path.join(valid_folder,"images"))
    shutil.copy(label_path, os.path.join(valid_folder,"labels"))
