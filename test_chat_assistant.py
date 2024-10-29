import unittest
from chat_assistant import ChatAssistant

class TestChatAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = ChatAssistant()

    def test_generate_response(self):
        response = self.assistant.generate_response("Hello!")
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main() 