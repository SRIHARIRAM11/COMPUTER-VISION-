import cv2
import numpy as np

def low_pass_filter(image_path, kernel_size=(3, 3)):
    # Load the image
    image = cv2.imread(image_path)

    # Apply average filter (box filter)
    averaged_image = cv2.blur(image, kernel_size)

    # Show the original image and the filtered image
    cv2.imshow("Original Image", image)
    cv2.imshow("Averaged Image", averaged_image)

    # Wait for any key press to close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = "your_image.jpg"
kernel_size = (5, 5)  # You can adjust the kernel size as needed
low_pass_filter(image_path, kernel_size)
