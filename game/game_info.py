import time

from screen.window import Window
from info_pixels.coordinate_pixel import CoordinatePixel
from info_pixels.facing_pixel import FacingPixel
from exceptions import WindowMissingError


class GameInfo:
    """Singleton class

    Get instance only throw instance method!!!
    """

    _instance = None

    def __init__(self, window: Window):
        self.x = None
        self.y = None
        self.facing = None

        info = {
            "x": CoordinatePixel,
            "y": CoordinatePixel,
            "facing": FacingPixel
        }

        for key, func in info.items():
            setattr(self, key, func(window.left, window.top))
            time.sleep(1)

    @classmethod
    def instance(cls, window: Window = None):
        if cls._instance is None:
            if window is None:
                raise WindowMissingError
            cls._instance = cls(window)
        return cls._instance
