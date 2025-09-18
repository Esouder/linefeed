from .device_config import DeviceConfig
from .print_segment import PrintSegment, PrintSegmentStatus
from queue import Queue
import threading


class PrintHandler:
    def __init__(self, device_config: DeviceConfig):
        self._segment_queue: Queue[PrintSegment] = Queue()
        self._device_location = device_config.location
        self._runner_thread = threading.Thread(target=self._runner, daemon=True)
        self._next_print_id: int = 0
        self._print_requests: dict[str, PrintSegment] = {}

    def print(self, segment: PrintSegment) -> str:
        self._segment_queue.put(segment)
        print_id = str(self._next_print_id)
        self._print_requests[print_id] = segment
        self._next_print_id += 1
        return print_id

    def _runner(self):
        with open(self._device_location, "wb", buffering=0) as device_file:
            while True:
                segment = self._segment_queue.get()
                segment.status = PrintSegmentStatus.PRINTING
                try:
                    device_file.write(segment.print_data)
                    segment.status = PrintSegmentStatus.COMPLETED
                except Exception:
                    segment.status = PrintSegmentStatus.FAILED

    def start(self):
        self._runner_thread.start()

    def get_status(self, print_id: str) -> PrintSegmentStatus:
        segment = self._print_requests.get(print_id)
        if segment:
            return segment.status
        raise ValueError(f"No print request found with ID: {print_id}")
