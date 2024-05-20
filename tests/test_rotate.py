import unittest
import cv2

class ImageRotateTestCase(unittest.TestCase):

    def setUp(self):
        self.image_metadata = load_test_image_metadata.load_test_image_metadata()

    def test_image_rotate_360(self):
        image = load_image.load_image(self.image_metadata['path'])
        self.assertEqual(image, 360)