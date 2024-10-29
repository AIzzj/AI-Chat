import unittest
from image_processing import ImageProcessor

class MockImageModel:
    def process(self, image_path):
        return f"Processed image at {image_path}"

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor(MockImageModel())

    def test_process(self):
        result = self.processor.process("path/to/image.jpg")
        self.assertIn("Processed image", result)

if __name__ == '__main__':
    unittest.main() 