import numpy as np

from config import PI
from info_pixels.game_info_pixel import GameInfoPixel
from lib.utils import get_rgb_from_numpy


class FacingPixel(GameInfoPixel):
    def _process_pixels(self, pixels: np.ndarray):
        r, g, b = get_rgb_from_numpy(pixels, self.x, self.y)
        return b * 2 * PI / 255
