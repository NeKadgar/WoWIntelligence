from screen.window import Window
from screen.frame import Frame
from typing import Iterator


class WindowStream:
    def __init__(self, window: Window):
        self.window = window

    def get_stream(self) -> Iterator[Frame]:
        while True:
            yield self.window.get_image()
