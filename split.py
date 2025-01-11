import os
import shutil
from sklearn.model_selection import train_test_split

# Source dataset directory containing your folders
source_dir = 'C:\\Users\\menuk\\Desktop\\New folder (8)'  # Update this path

# Target directories for train and validation sets
train_dir = 'New folder (4)'
val_dir = 'New folder (5)'

# Create directories for train and validation if they don’t exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Define your class names (folder names)
class_names = ['Paper', 'Rock', 'Scissors', 'Thumbs_up', 'Up']

# Iterate through each class and split images into train and validation sets
for class_name in class_names:
    class_path = os.path.join(source_dir, class_name)
    
    # List all image files in the class folder
    images = os.listdir(class_path)
    
    # Split images into training (80%) and validation (20%) sets
    train_images, val_images = train_test_split(images, test_size=0.2, random_state=42)
    
    # Create directories for the class in train and val folders
    train_class_dir = os.path.join(train_dir, class_name)
    val_class_dir = os.path.join(val_dir, class_name)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)
    
    # Move training images to the train directory
    for image in train_images:
        shutil.move(os.path.join(class_path, image), os.path.join(train_class_dir, image))
    
    # Move validation images to the val directory
    for image in val_images:
        shutil.move(os.path.join(class_path, image), os.path.join(val_class_dir, image))
