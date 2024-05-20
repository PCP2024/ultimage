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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
    else:
        image_path = sys.argv[1]
        load_image(image_path)
