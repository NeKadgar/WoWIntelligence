import sdl2.ext
import sdl2


class Display(object):
    def __init__(self, width: int, height: int):
        sdl2.ext.init()

        self.W, self.H = width, height
        self.window = sdl2.ext.Window("WOW", size=(width, height))
        self.window.show()

    def paint(self, image):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        # draw
        surf = sdl2.ext.pixels3d(self.window.get_surface())
        surf[:, :, 0:4] = image.swapaxes(0, 1)
        self.window.refresh()
