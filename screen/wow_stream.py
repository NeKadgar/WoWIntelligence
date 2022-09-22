from screen.window import Window


class WindowStream:
    def __init__(self, window: Window):
        self.window = window

    def get_stream(self):
        while True:
            yield self.window.get_image()
