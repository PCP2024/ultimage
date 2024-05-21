import unittest
import cv2

class ImageRotateTestCase(unittest.TestCase):

    def setUp(self):
        self.image_metadata = demodata.load_test_image_metadata.load_test_image_metadata()
        self.image = dataio.load_image.load_image(self.image_metadata['path'])

    def test_image_rotate_360(self):
        self.assertEqual(self.image, 360)