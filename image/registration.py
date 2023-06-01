import os
import shutil
import cv2
import numpy as np

def image_registration(file_from, file_to, save_path):
    # Load images
    img1 = cv2.imread(file_from)
    img2 = cv2.imread(file_to)

    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Initialize the ORB 
    orb = cv2.ORB_create()

    # Detector and compute keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    # Create a Brute-Force matcher object and match the descriptors
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    # Calculate transformation matrix based on matching results
    src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Transform the first image to align with the second image
    result = cv2.warpPerspective(img1, M, (img2.shape[1], img2.shape[0]))

    # Save result
    cv2.imwrite(save_path, result)

def image_registration_dir(input_fold_path, output_fold_path):
    # Make dirs
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    # Array to store file paths
    file_paths = []

    # Traverse all files in the folder
    for root, dirs, files in os.walk(input_fold_path):
        for file in files:
            # Generate the full path of the file
            file_path = os.path.join(root, file)
            # Append the file path to the array
            file_paths.append(file_path)

    for i in range(len(file_paths)) :
        file_from = file_paths[i]
        file_to = file_paths[0]
        save_path = output_fold_path + os.path.basename(file_from)

        image_registration(file_from, file_to, save_path)

# test
#input_path = './data/image/registration/input/'
#output_path = './data/image/registration/output/'
#image_registration_dir(input_path, output_path)