from screen.frame import Frame


class BaseInfoSensor:
    def __init__(self, name: str, x: int = None, y: int = None):
        self.value = None
        self.x = x
        self.y = y
        self.name = name
        print(name, x, y)

    def set_position(self, x: int, y: int):
        self.x, self.y = x, y
        print(f"Successfully set {self.name}", self.x, self.y)

    def print_value(self):
        print(f"{self.name}: {self.value}")

    def set_value(self, frame: Frame):
        self.value = self._process_pixels(frame)

    def _process_pixels(self, frame: Frame):
        raise NotImplementedError
