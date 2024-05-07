import skimage as ski
from matplotlib import  pyplot as plt
import cv2

def img_loader():
    filepath = input("type image path:")
    image_show = ski.io.imshow(filepath)
    plt.show()
    image = ski.io.imread(filepath)
    im = cv2.imread(filepath)

    print(type(im))

    print(im.shape)
    print(type(im.shape))

    print('the image',filepath,'was loaded')
    return image

img_loader()
