import unittest
from unittest.mock import patch, MagicMock
from pydantic import BaseModel
from intelligence.intelligence_router import IntelligenceRouter

class Person(BaseModel):
    name: str
    age: int

class TestIntelligenceRouter(unittest.TestCase):
    def setUp(self):
        self.router = IntelligenceRouter()

    @patch("intelligence.intelligence_router.NeedlesCapabilities.is_available", new_callable=unittest.mock.PropertyMock)
    def test_capabilities_discovery(self, mock_is_available):
        mock_is_available.return_value = True
        caps = self.router.get_capabilities()
        self.assertIn("EXTRACT", caps)
        self.assertIn("ACT", caps)
        self.assertIn("EMBED", caps)

    def test_fail_closed_decide(self):
        res = self.router.decide(context={"action": "reboot"})
        self.assertEqual(res["decision"], "DENIED")
        self.assertIn("requires explicit evidence", res["reason"])

    def test_decide_with_evidence(self):
        res = self.router.decide(context={"action": "reboot"}, evidence=["Load avg is 50.0"])
        self.assertEqual(res["decision"], "APPROVED")

    @patch("intelligence.intelligence_router.NeedlesCapabilities.extract")
    def test_extract(self, mock_extract):
        mock_extract.return_value = Person(name="John", age=30)
        res = self.router.extract("My name is John and I am 30 years old.", schema=Person)
        self.assertIsNotNone(res)
        self.assertEqual(res.name, "John")
        self.assertEqual(res.age, 30)
        mock_extract.assert_called_once_with("My name is John and I am 30 years old.", Person)

    @patch("intelligence.intelligence_router.NeedlesCapabilities.embed")
    def test_embed(self, mock_embed):
        mock_embed.return_value = [0.1, 0.2, 0.3]
        res = self.router.embed("Hello world")
        self.assertIsInstance(res, list)
        self.assertEqual(len(res), 3)
        mock_embed.assert_called_once_with("Hello world")

if __name__ == '__main__':
    unittest.main()
