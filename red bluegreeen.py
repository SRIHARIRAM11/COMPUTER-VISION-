import cv2

# Read the image
image = cv2.imread('man.jpg')

# Split the image into its RGB components
blue, green, red = cv2.split(image)

# Display each component separately
cv2.imshow('Red Component', red)
cv2.imshow('Green Component', green)
cv2.imshow('Blue Component', blue)

# Wait for any key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
