import json
import numpy as np
import unittest
import dataio.load_image as load
import processing.blur as blur

class ResizeTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = load.load_test_image_metadata()
        self.image = load.load_image(self.image_metadata['path'])
        self.image_dimensions = self.image_metadata['dimensions']

    def test_import(self):
        # Test module import
        import processing.blur as blur

    def test_blur_box(self):
        # Test that enlarge returns an image
        blurred = blur.normalized_box(self.image,(10,10))
        self.assertIsNotNone(blurred)

    def test_blur_gaussian(self):
        # Test that enlarge returns an image
        blurred = blur.gaussian(self.image,(5,5),0)
        self.assertIsNotNone(blurred)