import unittest
import numpy as np
import dataio.load_image as load
import processing.crop as crop

class CropImageTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = load.load_test_image_metadata()
        self.coords = [0,50,0,100]
        self.image = load.load_image(self.image_metadata['path'])
        self.image_dimensions = self.image_metadata['dimensions']

    def test_import(self):
        # Test module import
        import processing.crop as crop

    def test_cropped_image_type(self):
        # Test that the cropped image is a numpy array
        cropped_image = crop.image_crop(self.image, self.coords)
        self.assertTrue(isinstance(cropped_image, np.ndarray))

    def test_crop_dimensions(self):
        # Test that load_image returns something
        expected_dims = ((self.coords[1] - self.coords[0]), (self.coords[3] - self.coords[2]), self.image_dimensions[2])
        true_dims = crop.image_crop(self.image, self.coords).shape
        self.assertEqual(true_dims, expected_dims)

    def test_cropped_image_function(self):
        # Test that the cropped image values are correct
        cropped_image = crop.image_crop(self.image, self.coords)
        manual_crop = self.image[self.coords[0]:self.coords[1], self.coords[2]:self.coords[3]]
        comparison = np.array_equal(cropped_image, manual_crop)
        self.assertEqual(comparison, True) 