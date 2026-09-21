import unittest
from .needle_adapter import Needle3Adapter

class TestNeedle3Adapter(unittest.TestCase):
    def test_execute(self):
        adapter = Needle3Adapter()
        result = adapter.execute("EXTRACT", {"text": "hello"})
        self.assertEqual(result["status"], "executed")
        self.assertEqual(result["action"], "EXTRACT")
        self.assertEqual(result["provider"], "Needle 3.0.0")

if __name__ == '__main__':
    unittest.main()
