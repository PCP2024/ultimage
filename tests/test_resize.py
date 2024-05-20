import json
import numpy as np
import unittest

class ResizeTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = self.load_test_image_metadata()
        self.factor = 2
        self.image = load_image.load_image(self.image_metadata['path'])
        self.image_dimensions = self.image_metadata['dimensions']

    def test_import(self):
        # Test module import
        import processing.resize as resize

    def test_enlarge(self):
        # Test that enlarge returns an image
        enlarged = resize.enlarge(self.image,self.factor)
        self.assertIsInstance(enlarged, np.ndarray)

    def test_enlarge_dimensions(self):
        # Test that enlarge returns an image with the expected dimensions
        enlarged = resize.enlarge(self.image,self.factor)
        self.assertEqual(enlarged.shape, (self.factor*self.image_dimensions[0],self.factor*self.image_dimensions[0]))

    def test_shrink(self):
        # Test that shrink returns something
        shrunk = resize.shrink(self.image,self.factor)
        self.assertIsNotNone(shrunk)

    def test_shrink_dimensions(self):
        # Test that shrink returns an image with the expected dimensions
        shrunk = resize.shrink(self.image,self.factor)
        self.assertEqual(shrunk.shape, (self.image_dimensions[0]//self.factor,self.image_dimensions[0]//self.factor))