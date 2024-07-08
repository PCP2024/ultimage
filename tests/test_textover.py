import numpy as np
import unittest
import dataio.load_image as load
import processing.textover as textover
from configuration.config import load_defaults

class TextoverTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = load.load_test_image_metadata()
        self.image = load.load_image(self.image_metadata['path'])
        self.image_dimensions = self.image_metadata['dimensions']
        self.defaults = load_defaults()

    def test_import(self):
        # Test module import
        import processing.textover as textover

    def test_textover(self):
        # Test that textover returns an image
        texted = textover.textover(self.image,self.defaults['default_processing']['text'],self.defaults['default_font']['coordinates'])
        self.assertIsInstance(texted, np.ndarray)

    def test_textover_dimensions(self):
        # Test that textover returns the same image when text added out of bounds
        texted = textover.textover(self.image,self.defaults['default_processing']['text'],self.defaults['default_font']['coordinates'])
        comparison = np.array_equal(self.image, texted)
        self.assertEqual(self.image.shape, texted.shape)

    def test_textover_different(self):
        # Test that textover returns the same image when text added out of bounds
        texted = textover.textover(self.image,self.defaults['default_processing']['text'],self.defaults['default_font']['coordinates'])
        comparison = np.array_equal(self.image, texted)
        self.assertEqual(comparison,0)