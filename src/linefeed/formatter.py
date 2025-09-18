from .format_config import FormatConfig
from .print_command import PrintCommand
from .print_segment import PrintSegment


class Formatter:
    def __init__(self, format_config: FormatConfig):
        pass

    def format(self, command: PrintCommand) -> PrintSegment:
        pass
