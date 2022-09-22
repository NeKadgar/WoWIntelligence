import numpy as np


def get_rgb_from_numpy(np_array: np.ndarray, cord_x: int, cord_y: int):
    return np_array[cord_x][cord_y]
