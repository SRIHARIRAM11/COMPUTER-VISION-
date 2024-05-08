import cv2

def high_pass_sobel_filter(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel operator to compute gradients
    sobel_x = cv2.Sobel(grayscale_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(grayscale_image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the magnitude of gradients
    magnitude = cv2.magnitude(sobel_x, sobel_y)

    # Normalize the magnitude to 0-255
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Show the original image and the high-pass filtered image
    cv2.imshow("Original Image", image)
    cv2.imshow("High-Pass Filtered Image (Sobel)", magnitude)

    # Wait for any key press to close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = "your_image.jpg"
high_pass_sobel_filter(image_path)
