import unittest
import cv2

class ImageRotateTestCase(unittest.TestCase):

    image = cv2.imread("demodata/test.png")

    def test_image_rotate(self):
        pass
        

t = ImageRotateTestCase()
cv2.imshow("Image", t.image)
cv2.waitKey(0)

