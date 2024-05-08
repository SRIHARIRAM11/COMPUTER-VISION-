import cv2

def background_subtraction(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Create a background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(image)

    # Show the original image and the foreground mask
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Mask", fg_mask)

    # Wait for any key press to close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = "man.jpg"
background_subtraction(image_path)
