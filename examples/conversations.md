# Example conversations

## 1. Grounding with a healthcare FAQ
**User:** What is your cancellation policy?

**Assistant:** Patients should cancel or reschedule appointments as early as possible. For this demo, cancellations made at least 24 hours before the appointment do not incur a cancellation fee.

**Demonstrates:** The answer is retrieved from the local FAQ and the source section is exposed.

## 2. Identifying when a tool is needed
**User:** Can you cancel my appointment for Tuesday at 2 PM?

**Assistant:** I can request cancellation of Tuesday at 2 PM. Would you like me to proceed?

**Demonstrates:** The assistant identifies an action request instead of treating it as a normal FAQ question.

## 3. Confirmation before an action
**User:** Yes, please.

**Assistant:** Mock cancellation completed for Tuesday at 2 PM.

**Demonstrates:** The tool is not called until the user explicitly confirms.

## 4. Handling a question it cannot safely answer
**User:** I've had chest pain for three hours. What medication should I take?

**Assistant:** I can't diagnose symptoms or recommend treatment. If this may be an emergency, contact local emergency services or seek appropriate emergency care.

**Demonstrates:** The assistant does not invent a diagnosis or medication recommendation.
