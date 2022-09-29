import sdl2.ext
import sdl2
from enum import Enum
from application_types import PixelsArray


class DisplayType(Enum):
    RGBA = 'RGBA'
    RGB = 'RGB'
    BGR = 'BGR'


class Display(object):
    def __init__(self, width: int, height: int, display_type: DisplayType):
        sdl2.ext.init()

        self.W, self.H = width, height
        self.window = sdl2.ext.Window("WOW", size=(width, height))
        self.display_type = display_type
        self.window.show()

    def paint(self, image: PixelsArray):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        # draw
        surf = sdl2.ext.pixels3d(self.window.get_surface())

        if self.display_type in (DisplayType.BGR, DisplayType.RGB):
            surf[:, :, 0:3] = image.swapaxes(0, 1)
        elif self.display_type == DisplayType.RGB:
            surf[:, :, 0:4] = image.swapaxes(0, 1)

        self.window.refresh()
