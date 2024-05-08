import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the histogram
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot histogram
plt.plot(histogram)
plt.title('Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
