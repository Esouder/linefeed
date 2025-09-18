from pydantic import BaseModel


class FormatConfig(BaseModel):
    special_chars: dict[str, bytes] = (
        {}
    )  # What non-basic ASCII characters to allow (and the correct byte sequence for them).
    # Note that a byte sequence in the normal ASCII range (0-127) will override the default.
    unsupported_chars: list[str] = []  # Standard ASCII characters to disallow.
    max_line_length: int
    lines_per_page: int
    line_ending: bytes  # E.g. b"\n" or b"\r\n"
    page_ending: bytes  # E.g. b"\f" or b"\n\n"
    bell: bytes  # E.g. b"\x07"
    underline_start: bytes  # E.g. b"\x1b[4m"
    underline_end: bytes  # E.g. b"\x1b[24m"
    bold_start: bytes  # E.g. b"\x1b[1m"
    bold_end: bytes  # E.g. b"\x1b[22m"
