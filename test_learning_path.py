import unittest
from learning_path import LearningPathGenerator

class TestLearningPathGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = LearningPathGenerator()

    def test_generate_path(self):
        path = self.generator.generate_path("user123", ["goal1", "goal2"])
        self.assertIsInstance(path, list)

if __name__ == '__main__':
    unittest.main() 