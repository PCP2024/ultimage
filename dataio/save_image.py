from skimage import io

def save_image(image, image_path):
    try:
        io.imsave(image_path, image)
    except Exception as e:
        print("Error:", e)