import cv2

from screen.frame import Frame
from screen.window import Window
from exceptions import ForbiddenMethod, NoMoreFrames


class VideoWindow(Window):
    def __init__(self, filename: str):
        self._cap = cv2.VideoCapture(f"{filename}.avi")
        self.height, self.width = self._get_size()

    def _get_size(self):
        return self._get_next_frame().get_size()

    def _get_next_frame(self):
        if self._cap.isOpened():
            success, image = self._cap.read()
            if success:
                return Frame(image)
        raise NoMoreFrames

    def get_image(self):
        return self._get_next_frame()

    @classmethod
    def from_dragged_zone(cls):
        raise ForbiddenMethod
