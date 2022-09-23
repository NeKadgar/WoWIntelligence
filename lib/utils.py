import numpy as np
import keyboard
import mouse
import time


def get_rgb_from_numpy(np_array: np.ndarray, cord_x: int, cord_y: int):
    rgb = np_array[cord_x][cord_y]
    if len(rgb) == 3:
        return *rgb, 1
    return rgb


def get_absolute_cursor_position(key: str):
    while True:
        if keyboard.is_pressed(key):
            x, y = mouse.get_position()
            return x, y
        time.sleep(0.1)  # delay to not DDoS


def drag_and_get_box(key: str):
    """Return Top, Left, Width, Height"""

    while True:
        if keyboard.is_pressed(key):
            x1, y1 = mouse.get_position()
            print(x1, y1)
            while True:
                if not keyboard.is_pressed(key):
                    x2, y2 = mouse.get_position()
                    return y1, x1, x2 - x1, y2 - y1
                time.sleep(0.1)  # delay to not DDoS
        time.sleep(0.1)  # delay to not DDoS
