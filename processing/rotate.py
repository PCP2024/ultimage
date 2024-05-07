import numpy as np
import cv2

def rotate_image(image, angle):
    """
    Rotate an image represented as a numpy array.

    Parameters:
        image (numpy.ndarray): Input image as a numpy array.
        angle (float): Angle of rotation in degrees.

    Returns:
        numpy.ndarray: Rotated image.
    """
    # Get image shape
    h, w = image.shape[:2]

    # Calculate rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)

    # Apply rotation to image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

    return rotated_image