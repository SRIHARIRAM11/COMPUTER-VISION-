import cv2

# Read the image
image = cv2.imread('man.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the image to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display the original, grayscale, and HSV images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('HSV Image', hsv_image)

# Wait for any key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
