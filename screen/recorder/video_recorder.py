import cv2

from screen.frame import Frame
from screen.recorder.frame_queue import FrameQueue


class VideoRecorder:
    def __init__(self, filename: str, width: int, height: int, fps: int):
        self.width, self.height = width, height
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self._out = cv2.VideoWriter(f'{filename}.avi', fourcc, fps, (width, height), 1)

    def add_frame(self, frame: Frame):
        self._out.write(frame.get_rbg())

    def release(self):
        self._out.release()

    @classmethod
    def create_video_from_queue(cls, queue: FrameQueue, filename: str, fps: int = None):
        height, width = queue.queue[0].frame.get_size()  # bruh
        recorder = cls(filename, width, height, fps or queue.average_fps())
        for frame in queue.queue:
            recorder.add_frame(frame.frame)
        recorder.release()
