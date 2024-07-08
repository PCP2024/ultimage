import cv2

def image_crop(image, coords):
    x_start, x_end, y_start, y_end = coords
    new_x = x_end - x_start
    new_y = y_end - y_start

    crop_image = image[x_start:x_end, y_start:y_end]
    return crop_image

def crop_or_pad_image(image, x, y, width, height, pad_color=(255,255,255)):
    img_height, img_width = image.shape[:2]

    # Calculate the right and bottom coordinates
    right = x + width
    bottom = y + height

    # Determine padding amounts
    top_pad = max(0, -y)
    left_pad = max(0, -x)
    bottom_pad = max(0, bottom - img_height)
    right_pad = max(0, right - img_width)

    # Apply padding if necessary
    if top_pad > 0 or left_pad > 0 or bottom_pad > 0 or right_pad > 0:
        image = cv2.copyMakeBorder(image, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=pad_color)
        # Update the coordinates after padding
        x += left_pad
        y += top_pad

    # Crop the image
    cropped_image = image[y:y+height, x:x+width]

    return cropped_image
