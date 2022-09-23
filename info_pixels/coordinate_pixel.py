import numpy as np

from info_pixels.game_info_pixel import GameInfoPixel
from lib.utils import get_rgb_from_numpy


class CoordinatePixel(GameInfoPixel):
    def _process_pixels(self, pixels: np.ndarray):
        r, g, b, _ = get_rgb_from_numpy(pixels, self.x, self.y)
        print(r, g, b)
        return (r + g / 255) / 255 * 100
