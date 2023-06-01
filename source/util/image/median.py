import os
import cv2
import numpy as np

# Set folder path and save file name
folder_path = "data/registration/output"
save_filename = "data/registration/median_image.jpg"

# Get paths of all files in the folder and sort them alphabetically
file_paths = sorted([os.path.join(folder_path, file) for file in os.listdir(folder_path)])

# Read all images into a list
images = [cv2.imread(file_path, cv2.IMREAD_COLOR) for file_path in file_paths]

# Compute median pixel values
median_image = np.median(images, axis=0).astype(np.uint8)

# Save median image
cv2.imwrite(save_filename, median_image)