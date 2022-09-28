from info_pixels.game_info_pixel import GameInfoPixel
from screen.frame import Frame


class TargetAttackRangePixel(GameInfoPixel):
    def _process_pixels(self, frame: Frame):
        r, g, b = frame.get_pixel_rgb(self.x, self.y)
        return b
