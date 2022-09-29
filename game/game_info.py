from info_pixels.info_pixel_initializer import InfoPixelInitializer
from screen.frame import Frame
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
        self._init_info_pixels(window)

    def _init_info_pixels(self, window):
        frame = window.get_image()
        InfoPixelInitializer(frame, self.info)
        for name, sensor in self.info.items():
            setattr(self, name, sensor)

    def __getattr__(self, item) -> GameInfoPixel:
        if info := self.info.get(item) is None:
            raise NotFoundInfoPixel
        return info

    def update(self, frame: Frame):
        for name in self.info.keys():
            pixel: GameInfoPixel = getattr(self, name)
            pixel.set_value(frame)
            pixel.print_value()

    @classmethod
    def instance(cls, window: Window = None):
        if cls._instance is None:
            if window is None:
                raise WindowMissingError
            cls._instance = cls(window)
        return cls._instance
