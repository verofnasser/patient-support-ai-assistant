from dataclasses import dataclass
from pathlib import Path
import re

@dataclass
class FAQEntry:
    title: str
    body: str

class KnowledgeBase:
    """Small local FAQ retriever used to demonstrate grounding."""
    def __init__(self, path: str = "faq.md") -> None:
        self.path = Path(path)
        self.entries = self._load()

    def _load(self) -> list[FAQEntry]:
        text = self.path.read_text(encoding="utf-8")
        sections = re.split(r"(?m)^## ", text)
        entries = []
        for section in sections[1:]:
            lines = section.strip().splitlines()
            if lines:
                entries.append(FAQEntry(lines[0].strip(), "\n".join(lines[1:]).strip()))
        return entries

    @staticmethod
    def _tokens(text: str) -> set[str]:
        return set(re.findall(r"[a-z0-9]+", text.lower()))

    def search(self, query: str) -> FAQEntry | None:
        query_tokens = self._tokens(query)
        if not query_tokens:
            return None
        scored = []
        for entry in self.entries:
            score = len(query_tokens & self._tokens(f"{entry.title} {entry.body}"))
            scored.append((score, entry))
        score, entry = max(scored, key=lambda item: item[0], default=(0, None))
        return entry if score > 0 else None
