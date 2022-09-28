from config import PI
from info_pixels.game_info_pixel import GameInfoPixel
from screen.frame import Frame


class FacingPixel(GameInfoPixel):
    def _process_pixels(self, frame: Frame):
        r, g, b = frame.get_pixel_rgb(self.x, self.y)
        return b * 2 * PI / 255
