import unittest
from music_generation import MusicGenerator

class MockMusicModel:
    def generate(self, description, duration):
        return f"Music generated with description: {description} and duration: {duration}"

class TestMusicGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = MusicGenerator(MockMusicModel())

    def test_generate(self):
        music = self.generator.generate("A happy tune", 5)
        self.assertIn("Music generated", music)

if __name__ == '__main__':
    unittest.main() 