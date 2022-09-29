import numpy as np
import keyboard
import pyautogui
import time


def get_rgb_from_numpy(np_array: np.ndarray, cord_x: int, cord_y: int):
    b, g, r = np_array[cord_y][cord_x][:3]
    return r, g, b


def get_absolute_cursor_position(key: str):
    while True:
        if keyboard.is_pressed(key):
            x, y = pyautogui.position()
            return x, y
        time.sleep(0.1)  # delay to not DDoS


def drag_and_get_box(key: str):
    """Return Top, Left, Width, Height"""

    while True:
        if keyboard.is_pressed(key):
            x1, y1 = pyautogui.position()
            while True:
                if not keyboard.is_pressed(key):
                    x2, y2 = pyautogui.position()
                    return y1, x1, x2 - x1, y2 - y1
                time.sleep(0.1)  # delay to not DDoS
        time.sleep(0.1)  # delay to not DDoS
