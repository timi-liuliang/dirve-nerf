import cv2
import numpy as np

# Load images
img1 = cv2.imread('data/image1.png')
img2 = cv2.imread('data/target.png')

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

# Show result
cv2.imshow("Registered Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()