import cv2
import skimage as ski
from matplotlib import  pyplot as plt
import os

def blur_normalized_box(image,ksize):
    return cv2.blur(image,ksize)

def blur_gaussian(image,ksize,sigmaX):
    return cv2.GaussianBlur(image,ksize,sigmaX)