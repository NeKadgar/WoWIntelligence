import numpy as np
import pyautogui
from screen.frame import Frame
from screen.window import Window


class PyautoguiWindow(Window):
    def get_image(self):
        pixels_array = np.array(
            pyautogui.screenshot(region=(self.top, self.left, self.width, self.height))
        )
        return Frame(pixels_array)
