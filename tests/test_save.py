import os
import unittest
import dataio.load_image as load
import dataio.save_image as save

class SaveImageTestCase(unittest.TestCase):
    def setUp(self):
        self.image_metadata = load.load_test_image_metadata()
        self.image = load.load_image(self.image_metadata['path'])

    def test_import(self):
        # Test module import
        import dataio.save_image as save

    def test_save_image(self):
        # Test that save_image returns something
        save.save_image(self.image, 'test.jpg')
        self.assertIsNotNone(load.load_image('test.jpg'))
        # Delete saved image
        os.remove('test.jpg')