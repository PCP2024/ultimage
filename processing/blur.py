import cv2
import skimage as ski
from matplotlib import  pyplot as plt
import os

def normalized_box(image,ksize):
    return cv2.blur(image,ksize)

def gaussian(image,ksize,sigmaX):
    return cv2.GaussianBlur(image,ksize,sigmaX)