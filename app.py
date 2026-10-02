from src.assistant import PatientSupportAssistant


def main() -> None:
    assistant = PatientSupportAssistant()
    print("Patient Support AI Assistant")
    print("Type 'quit' to exit. This is an educational prototype, not medical advice.\n")

    while True:
        message = input("You: ").strip()
        if message.lower() in {"quit", "exit"}:
            print("Assistant: Goodbye!")
            break
        response = assistant.respond(message)
        print(f"Assistant: {response.text}")
        if response.source:
            print(f"  [Grounded in: {response.source}]")
        if response.action:
            print(f"  [Action status: {response.action.status}]")
        print()


if __name__ == "__main__":
    main()
