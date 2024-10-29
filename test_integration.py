import unittest
from api_management import app
from emotion_analysis import EmotionAnalyzer

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.analyzer = EmotionAnalyzer()

    def test_emotion_analysis_integration(self):
        # 模拟API调用
        response = self.app.post('/analyze_emotion', json={'text': 'I am very happy today!'})
        self.assertEqual(response.status_code, 200)
        
        # 获取API返回的情感
        api_emotion = response.json.get('emotion')
        
        # 使用情感分析模块直接分析
        direct_emotion = self.analyzer.analyze('I am very happy today!')
        
        # 验证API返回的情感与直接分析的结果一致
        self.assertEqual(api_emotion, direct_emotion)

if __name__ == '__main__':
    unittest.main() 