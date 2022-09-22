import numpy as np
import pyautogui


class PyautoguiWindow:
    def __init__(self, top: int, left: int, width: int, height: int):
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    def get_image(self):
        return np.array(
            pyautogui.screenshot(region=(self.top, self.left, self.width, self.height))
        )
