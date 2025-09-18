from .format_config import FormatConfig
from .print_command import PrintCommand
from .print_segment import PrintSegment


class Formatter:
    def __init__(self, format_config: FormatConfig):
        self._config = format_config

    def format(self, command: PrintCommand) -> PrintSegment:
        """
        Formats a PrintCommand into a PrintSegment according to the specified FormatConfig.
        This includes handling special characters, unsupported characters, line wrapping,
        and adding appropriate line and page endings.

        Parameters
        ----------
        command : PrintCommand
            The command containing text content and formatting options.

        Returns
        -------
        PrintSegment
            The formatted print segment ready for printing.
        """
        lines: list[str] = []
        for line in command.text_content.splitlines():
            # Replace special characters
            for char, byte_seq in self._config.special_chars.items():
                line = line.replace(char, byte_seq.decode("ascii", errors="ignore"))

            for char in line:
                if char in self._config.unsupported_chars:
                    raise ValueError(f"Unsupported character found: {char}")

            # Wrap or truncate lines
            if command.wrap_text:
                wrapped_lines = self.wrap_line(line, self._config.max_line_length)
                lines.extend(wrapped_lines)
            else:
                lines.append(line[: self._config.max_line_length])

        # Add line endings
        formatted_content = (
            self._config.line_ending.join(
                line.encode("ascii", errors="ignore") for line in lines
            )
            + self._config.line_ending
        )

        # Add page ending if eject_page is True
        if command.eject_page:
            formatted_content += self._config.page_ending

        # Add bell if forebell is True
        if command.forebell:
            formatted_content = self._config.bell + formatted_content

        if len(lines) > self._config.lines_per_page:
            raise ValueError(
                f"Content exceeds maximum lines per page: {self._config.lines_per_page}"
            )
        return PrintSegment(print_data=formatted_content)

    @staticmethod
    def wrap_line(line: str, max_length: int) -> list[str]:
        """
        Wraps a single line of text into multiple lines based on the specified maximum length.

        Parameters
        ----------
        line : str
            The line of text to be wrapped.
        max_length : int
            The maximum length of each line.

        Returns
        -------
        list[str]
            A list of wrapped lines.
        """
        return [line[i : i + max_length] for i in range(0, len(line), max_length)]
