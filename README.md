# Patient Support AI Assistant

A small portfolio project demonstrating four practical AI assistant patterns: grounding with trusted knowledge, identifying when a tool/action is needed, asking for confirmation before an action, and safely handling questions outside the assistant's scope.

> **Important:** This is an educational prototype, not a medical device and not a substitute for a licensed healthcare professional.

## What this demonstrates

1. **Grounding:** routine support questions are answered from a local healthcare FAQ rather than invented policy information.
2. **Tool selection:** appointment-management requests are recognized as actions rather than ordinary questions.
3. **Confirmation:** a mock appointment action is not executed until the user explicitly confirms.
4. **Safety routing:** high-risk medical questions are not answered with diagnosis or treatment advice.

## Run locally

This demo uses only Python's standard library.

```bash
python app.py
```

Try `What is your cancellation policy?`, then `Can you cancel my appointment for Tuesday at 2 PM?`, followed by `Yes, please`.

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Architecture

```text
User message
     |
     v
Safety check ---- high-risk question ----> Safe-care response
     |
     v
Action intent? -- yes --> Pending action --> Confirmation --> Mock tool
     |
     no
     v
FAQ retrieval --> Grounded response + source
```

The FAQ is synthetic so this project does not depend on a real clinic or live patient data.

## Why I built it

I built this project to practice practical AI concepts that matter in support workflows: grounding, intent detection, tool use, confirmation gates, and safe handling of requests the system should not answer.

## Limitations and next steps

This prototype uses simple keyword and token matching rather than a production LLM. A real implementation would need stronger retrieval, authentication, audit logging, structured tool schemas, human escalation, privacy controls, and extensive safety evaluation.

A future version could connect the knowledge layer to Azure AI Search and add an Azure OpenAI or other LLM response layer while keeping the confirmation and safety gates explicit.
