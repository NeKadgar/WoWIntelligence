import numpy as np

from info_pixels.game_info_pixel import GameInfoPixel
from lib.utils import get_rgb_from_numpy


class StatisticPixel(GameInfoPixel):
    def _process_pixels(self, pixels: np.ndarray):
        r, g, b, _ = get_rgb_from_numpy(pixels, self.x, self.y)
        return sum((r, g, b))
