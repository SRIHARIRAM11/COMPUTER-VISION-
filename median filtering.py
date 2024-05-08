import cv2

def low_pass_median_filter(image_path, kernel_size=3):
    # Load the image
    image = cv2.imread(image_path)

    # Apply median filter
    median_filtered_image = cv2.medianBlur(image, kernel_size)

    # Show the original image and the filtered image
    cv2.imshow("Original Image", image)
    cv2.imshow("Median Filtered Image", median_filtered_image)

    # Wait for any key press to close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = "your_image.jpg"
kernel_size = 3  # You can adjust the kernel size as needed
low_pass_median_filter(image_path, kernel_size)
