def image_crop(image, coords):
    x_start, x_end, y_start, y_end = coords
    crop_image = image[x_start:x_end, y_start:y_end]
    return crop_image
