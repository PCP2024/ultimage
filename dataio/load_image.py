import json
import sys
from skimage import io

def load_image(image_path):
    try:
        image = io.imread(image_path)
        return image
    except Exception as e:
        print("Error:", e)

def show_image(image):
    io.imshow(image)
    io.show()

def load_test_image_metadata():
    # Load test image path from config.json
    with open('./configuration/config.json') as f:
        config = json.load(f)
        return config['test_image']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python load_image.py <image_path>")
    else:
        image_path = sys.argv[1]
        load_image(image_path)
