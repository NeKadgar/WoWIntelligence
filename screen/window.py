from lib.utils import drag_and_get_box
from screen.frame import Frame


class Window:
    def __init__(self, top: int, left: int, width: int, height: int):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def get_image(self) -> Frame:
        raise NotImplementedError

    @classmethod
    def from_dragged_zone(cls):
        key = "T"
        print(f"Hold {key} and draw target box")
        top, left, width, height = drag_and_get_box(key)
        return cls(top, left, width, height)
