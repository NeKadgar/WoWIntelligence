import time

from screen.window import Window
from info_pixels.game_info_pixel import GameInfoPixel
from info_pixels.coordinate_pixel import CoordinatePixel
from info_pixels.facing_pixel import FacingPixel
from exceptions import WindowMissingError, NotFoundInfoPixel


class GameInfo:
    """Singleton class

    Get instance only throw instance method!!!
    """

    _instance = None

    def __init__(self, window: Window):
        self.info = {
            "x": CoordinatePixel,
            "y": CoordinatePixel,
            "facing": FacingPixel
        }

        for name, func in self.info.items():
            setattr(self, name, func(name, window.left, window.top))
            time.sleep(1)

    def __getattr__(self, item) -> GameInfoPixel:
        if info := self.info.get(item) is None:
            raise NotFoundInfoPixel
        return info

    def update(self, image):
        for name in self.info.keys():
            pixel: GameInfoPixel = getattr(self, name)
            pixel.set_value(image)
            # pixel.print_value()

    @classmethod
    def instance(cls, window: Window = None):
        if cls._instance is None:
            if window is None:
                raise WindowMissingError
            cls._instance = cls(window)
        return cls._instance
