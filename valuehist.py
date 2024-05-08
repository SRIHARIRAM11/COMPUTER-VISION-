import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread('man.jpg', cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display the original and equalized images
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)

# Wait for any key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
