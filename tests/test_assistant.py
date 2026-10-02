import unittest
from src.assistant import PatientSupportAssistant

class TestPatientSupportAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = PatientSupportAssistant()

    def test_grounded_faq_answer(self):
        response = self.assistant.respond("What is your cancellation policy?")
        self.assertEqual(response.source, "Cancellation policy")
        self.assertIn("24 hours", response.text)

    def test_action_requires_confirmation(self):
        response = self.assistant.respond("Can you cancel my appointment for Tuesday at 2 PM?")
        self.assertIsNone(response.action)
        self.assertIn("Would you like me to proceed?", response.text)

    def test_confirmation_executes_mock_tool(self):
        self.assistant.respond("Can you cancel my appointment for Tuesday at 2 PM?")
        response = self.assistant.respond("Yes, please")
        self.assertIsNotNone(response.action)
        self.assertEqual(response.action.status, "completed")

    def test_high_risk_question_is_not_answered_medically(self):
        response = self.assistant.respond("I've had chest pain for three hours. What medication should I take?")
        self.assertIsNone(response.action)
        self.assertIn("can't diagnose", response.text)

    def test_unknown_question_is_not_invented(self):
        response = self.assistant.respond("What is my blood pressure supposed to be?")
        self.assertIsNone(response.source)
        self.assertIn("don't have enough trusted information", response.text)

if __name__ == "__main__":
    unittest.main()
