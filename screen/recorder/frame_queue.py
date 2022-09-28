import time
from dataclasses import dataclass
from typing import List

from screen.frame import Frame


@dataclass
class TimedFrame:
    frame: Frame
    time_per_frame: time.time


class FrameQueue:
    def __init__(self):
        self.queue: List[TimedFrame] = []
        self._time = None

    def last_frame_time(self):
        last_time = self._time or time.time()
        self._time = time.time()
        return last_time

    def add(self, frame: Frame):
        time_per_frame = time.time() - self.last_frame_time()
        self.queue.append(TimedFrame(frame, time_per_frame))

    def total_frames(self):
        return len(self.queue)

    def average_fps(self):
        total_time = sum(tf.time_per_frame for tf in self.queue)
        return 1.0 / (total_time / self.total_frames())
