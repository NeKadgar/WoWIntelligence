from screen.window import Window
from application_types import PixelsArray
from typing import Iterator


class WindowStream:
    def __init__(self, window: Window):
        self.window = window

    def get_stream(self) -> Iterator[PixelsArray]:
        while True:
            yield self.window.get_image()
