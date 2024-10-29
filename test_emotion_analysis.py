import unittest
from emotion_analysis import EmotionAnalyzer

class TestEmotionAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = EmotionAnalyzer()

    def test_analyze(self):
        text = "I am very happy today!"
        emotion = self.analyzer.analyze(text)
        self.assertIn(emotion, ["happy", "neutral", "sad", "joy"])  # 假设模型返回的情感类别

if __name__ == '__main__':
    unittest.main() 