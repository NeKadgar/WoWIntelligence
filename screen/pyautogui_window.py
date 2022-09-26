import numpy as np
import pyautogui
from screen.window import Window


class PyautoguiWindow(Window):
    def get_image(self):
        return np.array(
            pyautogui.screenshot(region=(self.top, self.left, self.width, self.height))
        )
