from sensors.base_info_sensor import BaseInfoSensor
from screen.frame import Frame


class CoordinateSensor(BaseInfoSensor):
    def _process_pixels(self, frame: Frame):
        r, g, b = frame.get_pixel_rgb(self.x, self.y)
        return (r + g / 255) / 255 * 100
