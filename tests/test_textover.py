import numpy as np
import unittest
import dataio.load_image as load
import processing.textover as textover

class TextoverTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = load.load_test_image_metadata()
        self.image = load.load_image(self.image_metadata['path'])
        self.image_dimensions = self.image_metadata['dimensions']
        self.text = "Hello, World!"

    def test_import(self):
        # Test module import
        import processing.textover as textover

    def test_textover(self):
        # Test that textover returns an image
        texted = textover.textover(self.image,self.text,10,10)
        self.assertIsInstance(texted, np.ndarray)

    def test_textover_dimensions(self):
        # Test that textover returns the same image when text added out of bounds
        texted = textover.textover(self.image,self.text,self.image_dimensions[0],self.image_dimensions[0])
        comparison = np.array_equal(self.image, texted)
        self.assertEqual(comparison,1)