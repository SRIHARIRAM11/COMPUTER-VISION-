import cv2

# Read the image
image = cv2.imread('man.jpg')

# Flip the image horizontally
flipped_horizontal = cv2.flip(image, 1)

# Flip the image vertically
flipped_vertical = cv2.flip(image, 0)

# Display the original and flipped images
cv2.imshow('Original Image', image)
cv2.imshow('Flipped Horizontally', flipped_horizontal)
cv2.imshow('Flipped Vertically', flipped_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
