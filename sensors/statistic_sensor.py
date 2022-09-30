from screen.frame import Frame
from sensors.base_info_sensor import BaseInfoSensor


class StatisticSensor(BaseInfoSensor):
    def _process_pixels(self, frame: Frame):
        r, g, b = frame.get_pixel_rgb(self.x, self.y)
        return sum((r, g, b))
