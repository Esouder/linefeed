from .device_config import DeviceConfig
from .print_segment import PrintSegment
from queue import Queue
import threading


class PrintHandler:
    def __init__(self, device_config: DeviceConfig):
        self._segment_queue: Queue[PrintSegment] = Queue()
        self._device_location = device_config.location
        self._runner_thread = threading.Thread(target=self._runner, daemon=True)

    def print(self, segment: PrintSegment):
        self._segment_queue.put(segment)

    def _runner(self):
        with open(self._device_location, "wb", buffering=0) as device_file:
            while True:
                segment = self._segment_queue.get()
                device_file.write(segment.print_data)

    def start(self):
        self._runner_thread.start()
