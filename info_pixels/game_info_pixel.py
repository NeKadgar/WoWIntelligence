import numpy as np


class GameInfoPixel:
    def __init__(self, x, y):
        self.value = None
        self.x = x
        self.y = y

    def set_value(self, pixels: np.array):
        self.value = self._process_pixels(pixels)

    def _process_pixels(self, pixels: np.array):
        raise NotImplementedError
