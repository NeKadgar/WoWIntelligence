from typing import Tuple, List

import cv2
from application_types import PixelsArray


class Frame:
    def __init__(self, image: PixelsArray):
        self.image = image

    def get_pixel_rgb(self, x, y):
        b, g, r = self.image[y][x][:3]
        return r, g, b

    def get_size(self):
        return self.image.shape[0], self.image.shape[1]

    def get_rbg(self):
        return cv2.cvtColor(self.image, cv2.COLOR_RGBA2RGB)  # noqa

    def get_bgr(self):
        return cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)  # noqa

    def get_grayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)  # noqa

    def draw_matches_lines(self, matches):
        image = self.image.copy()
        for p1, p2 in matches:
            u1, v1 = map(lambda x: int(round(x)), p1.pt)
            u2, v2 = map(lambda x: int(round(x)), p2.pt)
            image = cv2.line(image, (u1, v1), (u2, v2), (0, 0, 255), 2)  # noqa
        return image

    def matplot_draw_circles(self, circles: List[Tuple[int, int]]):
        image = self.get_matplot_format()
        for x, y in circles:
            image = cv2.circle(image, (x, y), 1, (255, 0, 0), 1)  # noqa
        return image

    def get_matplot_format(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)  # noqa
