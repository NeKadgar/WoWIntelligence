import numpy as np
from mss import mss

from screen.window import Window


class MSSWindow(Window):
    def __init__(self, top: int, left: int, width: int, height: int):
        super().__init__(top, left, width, height)
        self._monitor_data = self._get_monitor_data(top, left, width, height)

    def get_image(self):
        with mss() as sct:
            return np.array(
                sct.grab(self._monitor_data)
            )

    @staticmethod
    def _get_monitor_data(top: int, left: int, width: int, height: int):
        return {
            "top": top,
            "left": left,
            "width": width,
            "height": height,
        }
