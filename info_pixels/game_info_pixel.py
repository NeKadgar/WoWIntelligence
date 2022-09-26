import numpy as np
from lib.utils import get_absolute_cursor_position


class GameInfoPixel:
    def __init__(self, name: str, padding_x: int, padding_y: int):
        self.value = None
        x, y = self._init_position()
        self.x = x - padding_x
        self.y = y - padding_y
        self.name = name
        print(f"Successfully set {name}", self.x, self.y)

    @staticmethod
    def _init_position():
        key = "V"
        print(f"Move cursor to target position and then press {key}")
        return get_absolute_cursor_position(key)

    def print_value(self):
        print(f"{self.name}: {self.value}")

    def set_value(self, pixels: np.ndarray):
        self.value = self._process_pixels(pixels)

    def _process_pixels(self, pixels: np.ndarray):
        raise NotImplementedError
