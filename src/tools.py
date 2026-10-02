from dataclasses import dataclass

@dataclass
class ActionResult:
    action: str
    status: str
    message: str

def cancel_appointment(appointment: str) -> ActionResult:
    """Mock tool: completes a cancellation without touching a real system."""
    return ActionResult("cancel_appointment", "completed", f"Mock cancellation completed for {appointment}.")
