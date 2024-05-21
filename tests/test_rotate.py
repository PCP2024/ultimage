import unittest
import numpy as np
import demodata.load_test_image_metadata as dd
import dataio.load_image as load
import processing.rotate as rotate

class ImageRotateTestCase(unittest.TestCase):

    def setUp(self):
        self.image_metadata = dd.load_test_image_metadata(self)
        self.image = load.load_image(self.image_metadata['path'])

    def test_import(self):
        # Test module import
        import processing.rotate as rotate

    def test_image_rotate_360(self):
        rotated = rotate.rotate_image(self.image, 360)
        comparison = np.array_equal(self.image, rotated)
        self.assertEqual(comparison,1)

    def test_mirror_vertically(self):
        mirrored = rotate.mirror_image(self.image, 0)
        comparison = np.array_equal(self.image, rotate.mirror_image(mirrored, 0))
        self.assertEqual(comparison,1)

    def test_mirror_horizontally(self):
        mirrored = rotate.mirror_image(self.image, 1)
        comparison = np.array_equal(self.image, rotate.mirror_image(mirrored, 1))
        self.assertEqual(comparison,1)