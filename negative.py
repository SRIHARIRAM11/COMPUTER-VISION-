import cv2

# Read the image
image = cv2.imread('man.jpg')

# Calculate the negative of the image
negative_image = 255 - image

# Display the original and negative images
cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
