import cv2

# Read the image in grayscale
image = cv2.imread('man.jpg', cv2.IMREAD_GRAYSCALE)

# Apply a threshold
_, thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)

# Wait for any key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
