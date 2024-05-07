import json
import numpy as np
import unittest

class LoadImageTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = load_test_image_metadata.load_test_image_metadata()

    def test_import(self):
        # Test module import
        import dataio.load_image as load_image

    def test_load_image(self):
        # Test that load_image returns something
        image = load_image.load_image(self.image_metadata['path'])
        self.assertIsNotNone(image)

    def test_image_format(self):
        # Test that load_image returns a numpy array
        image = load_image.load_image(self.image_metadata['path'])
        self.assertIsInstance(image, np.ndarray)

    def test_image_dimensions(self):
        # Test that the image has expected dimensions
        image = load_image.load_image(self.image_metadata['path'])
        self.assertEqual(image.shape, self.image_metadata['dimensions'])