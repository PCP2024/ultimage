import json
import numpy as np
import unittest
import dataio.load_image as load
import analyze.blur as blur
from configuration.config import load_defaults

class ResizeTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = load.load_test_image_metadata()
        self.image = load.load_image(self.image_metadata['path'])
        self.image_dimensions = self.image_metadata['dimensions']
        self.ksize = load_defaults()['default_analysis']['ksize']
        self.sigma = load_defaults()['default_analysis']['gauss_sigma']

    def test_import(self):
        # Test module import
        import analyze.blur as blur

    def test_blur_box(self):
        # Test that enlarge returns an image
        blurred = blur.normalized_box(self.image,self.ksize)
        self.assertIsNotNone(blurred)

    def test_blur_gaussian(self):
        # Test that enlarge returns an image
        blurred = blur.gaussian(self.image,self.ksize,self.sigma)
        self.assertIsNotNone(blurred)