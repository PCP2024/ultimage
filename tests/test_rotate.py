import unittest
import cv2

class ImageRotateTestCase(unittest.TestCase):

    def setUp(self):
        self.image_metadata = demodata.load_test_image_metadata.load_test_image_metadata()
        self.image = dataio.load_image.load_image(self.image_metadata['path'])

    def test_import(self):
        # Test module import
        import processing.rotate as rotate

    def test_image_rotate_360(self):
        self.assertEqual(self.image, 360)

    def test_mirror_vertically(self):
        mirrored = rotate.mirror_image(self.image, 0)
        self.assertEqual(self.image, rotate.mirror_image(mirrored, 0))

    def test_mirror_horizontally(self):
        mirrored = rotate.mirror_image(self.image, 1)
        self.assertEqual(self.image, rotate.mirror_image(mirrored, 1))