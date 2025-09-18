from dataclasses import dataclass
from textwrap import wrap

from click import wrap_text


@dataclass
class PrintCommand:
    text_content: str
    eject_page: bool = False
    forebell: bool = False
    afterbell: bool = False
    wrap_text: bool = True  # Or just truncate.
