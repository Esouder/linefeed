from dataclasses import dataclass
from enum import Enum, auto


class PrintSegmentStatus(Enum):
    QUEUED = auto()
    PRINTING = auto()
    COMPLETED = auto()
    FAILED = auto()


@dataclass
class PrintSegment:
    """
    Represents a segment of data to be printed, along with its status.
    Attributes
    ----------
    print_data : bytes
        The raw data to be printed.
    status : PrintSegmentStatus
        The current status of the print segment. Defaults to `PrintSegmentStatus.QUEUED`.
    """

    print_data: bytes
    status: PrintSegmentStatus = PrintSegmentStatus.QUEUED
