import unittest
import sys
import cv2

sys.path.append("/ultimage/dataio")
filepath = input("type image path:")
filepath_crop = input("type CROPED image path:")

class MultiplyTestCase(unittest.TestCase):
    def test_img_size(self):
        im = cv2.imread(filepath)
        im_crop = cv2.imread(filepath_crop)
        
        self.assertEqual(im,im_crop)

    #def test_multiply_positive_numbers(self):
    #    result= multiply(3,4)
    #    self.assertEqual(result,12)
