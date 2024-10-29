import unittest
from academic_support import AcademicSupport

class TestAcademicSupport(unittest.TestCase):
    def setUp(self):
        self.support = AcademicSupport()

    def test_check_grammar(self):
        suggestions = self.support.check_grammar("This is a test sentence.")
        self.assertIsInstance(suggestions, list)

    def test_format_citations(self):
        formatted = self.support.format_citations("This is a citation.", style='APA')
        self.assertIn("(Author, Year)", formatted)

if __name__ == '__main__':
    unittest.main() 