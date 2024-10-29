import unittest
from video_processing import VideoProcessor

class TestVideoProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = VideoProcessor()

    def test_edit_video(self):
        result = self.processor.edit_video("path/to/video.mp4", 0, 10)
        self.assertEqual(result, "edited_video_path")

if __name__ == '__main__':
    unittest.main() 