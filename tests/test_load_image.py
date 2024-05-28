import json
import numpy as np
import unittest
import demodata.load_test_image_metadata as dd
import dataio.load_image as load

class LoadImageTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = dd.load_test_image_metadata(self)

    def test_import(self):
        # Test module import
        import dataio.load_image as load

    def test_load_image(self):
        # Test that load_image returns something
        image = load.load_image(self.image_metadata['path'])
        self.assertIsNotNone(image)

    def test_image_format(self):
        # Test that load_image returns a numpy array
        image = load.load_image(self.image_metadata['path'])
        self.assertIsInstance(image, np.ndarray)

    def test_image_dimensions(self):
        # Test that the image has expected dimensions
        image = load.load_image(self.image_metadata['path'])
        self.assertEqual(list(image.shape), self.image_metadata['dimensions'])