import cv2

def high_pass_laplacian_filter(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Laplacian operator
    laplacian = cv2.Laplacian(grayscale_image, cv2.CV_64F)

    # Normalize the Laplacian to 0-255
    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Show the original image and the high-pass filtered image
    cv2.imshow("Original Image", image)
    cv2.imshow("High-Pass Filtered Image (Laplacian)", laplacian)

    # Wait for any key press to close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = "man.jpg"
high_pass_laplacian_filter(image_path)
