import cv2
import skimage as ski
from matplotlib import  pyplot as plt
import os



def image_crop(imagepath, x_start, x_end, y_start, y_end):
    image = cv2.imread(imagepath)

    crop_image = image[x_start:x_end, y_start:y_end]

    image_show = ski.io.imshow(crop_image)
    plt.show()


    return crop_image

 
#if __name__ == '__main__':
#   path = os.getcwd()
#   os.chdir('..')
#   image_crop("demodata\\test.png", 1, 300, 1, 300)

#   image_crop("testimg.jpg", 1, 300, 1, 300)
