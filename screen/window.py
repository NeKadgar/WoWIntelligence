class Window:
    def __init__(self, top: int, left: int, width: int, height: int):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def get_image(self):
        raise NotImplementedError
