import numpy as np
from mss import mss

from screen.frame import Frame
from screen.window import Window


class MSSWindow(Window):
    def __init__(self, top: int, left: int, width: int, height: int):
        print(top, left, width, height)
        super().__init__(top, left, width, height)
        self._monitor_data = self._get_monitor_data(top, left, width, height)

    def get_image(self):
        with mss() as sct:
            pixels_array = np.array(
                sct.grab(self._monitor_data)
            )
            return Frame(pixels_array)

    @staticmethod
    def _get_monitor_data(top: int, left: int, width: int, height: int):
        return {
            "top": top,
            "left": left,
            "width": width,
            "height": height,
        }
