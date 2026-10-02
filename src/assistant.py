from dataclasses import dataclass
import re
from .knowledge_base import KnowledgeBase
from .tools import ActionResult, cancel_appointment

@dataclass
class AssistantResponse:
    text: str
    source: str | None = None
    action: ActionResult | None = None

class PatientSupportAssistant:
    """Rule-based prototype illustrating grounding, tools, confirmation, and safety."""
    HIGH_RISK_TERMS = {"chest pain", "difficulty breathing", "can't breathe", "cannot breathe", "stroke", "seizure", "overdose", "severe bleeding", "suicidal", "kill myself"}

    def __init__(self, faq_path: str = "faq.md") -> None:
        self.knowledge = KnowledgeBase(faq_path)
        self.pending_action: str | None = None

    def respond(self, message: str) -> AssistantResponse:
        text = message.strip()
        lower = text.lower()
        if self._is_high_risk(lower):
            self.pending_action = None
            return AssistantResponse("I can't diagnose symptoms or recommend treatment. If this may be an emergency, contact local emergency services or seek appropriate emergency care. For non-emergency concerns, contact a licensed healthcare professional.")
        if self.pending_action:
            if self._is_confirmation(lower):
                appointment = self.pending_action
                self.pending_action = None
                result = cancel_appointment(appointment)
                return AssistantResponse(result.message, action=result)
            if self._is_decline(lower):
                self.pending_action = None
                return AssistantResponse("Okay. I won't make the appointment change.")
            return AssistantResponse("I need a clear yes or no before I make the appointment change.")
        if self._is_cancel_request(lower):
            appointment = self._extract_appointment(text)
            self.pending_action = appointment
            return AssistantResponse(f"I can request cancellation of {appointment}. Would you like me to proceed?")
        entry = self.knowledge.search(text)
        if entry:
            return AssistantResponse(entry.body, source=entry.title)
        return AssistantResponse("I don't have enough trusted information in my FAQ to answer that safely. Please contact the clinic or a licensed healthcare professional for help.")

    @classmethod
    def _is_high_risk(cls, text: str) -> bool:
        return any(term in text for term in cls.HIGH_RISK_TERMS)

    @staticmethod
    def _is_cancel_request(text: str) -> bool:
        return bool(re.search(r"\b(cancel|cancellation)\b", text) and "appointment" in text)

    @staticmethod
    def _is_confirmation(text: str) -> bool:
        return bool(re.fullmatch(r"(yes|yes please|confirm|confirmed|go ahead|please do|proceed)[.! ]*", text))

    @staticmethod
    def _is_decline(text: str) -> bool:
        return bool(re.fullmatch(r"(no|no thanks|cancel that|never mind|don't|do not)[.! ]*", text))

    @staticmethod
    def _extract_appointment(text: str) -> str:
        match = re.search(r"(?:for|on)\s+(.+?)(?:\?|$)", text, flags=re.IGNORECASE)
        return match.group(1).strip() if match else "the requested appointment"
