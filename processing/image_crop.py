import cv2
import skimage as ski
from matplotlib import  pyplot as plt
import sys

sys.path.append("/ultimage/demodata")

filepath = input("type image path:")
im = cv2.imread(filepath)
print(im.shape)


#crop_img = img[y:y+h, x:x+w]
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)