from dataclasses import dataclass


@dataclass
class PrintCommand:
    text_content: str
    eject_page: bool = False
    forebell: bool = False
    wrap_text: bool = True  # Or just truncate.
