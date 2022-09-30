from sensors.info_sensors_builder import InfoSensorsBuilder
from screen.frame import Frame
from screen.window import Window
from sensors.base_info_sensor import BaseInfoSensor
from sensors.coordinate_sensor import CoordinateSensor
from sensors.facing_sensor import FacingSensor
from exceptions import WindowMissingError


class GameInfo:
    """Singleton class

    Get instance only throw instance method!!!
    """

    _instance = None

    def __init__(self, window: Window):
        self.info_schema = {
            "x": CoordinateSensor,
            "y": CoordinateSensor,
            "facing": FacingSensor
        }
        self._init_info_pixels(window)

    def _init_info_pixels(self, window):
        frame = window.get_image()
        sensors: dict = InfoSensorsBuilder.from_sensors_dict(frame, self.info_schema)
        for name, sensor in sensors.items():
            setattr(self, name, sensor)

    def update(self, frame: Frame):
        for name in self.info_schema.keys():
            pixel: BaseInfoSensor = getattr(self, name)
            pixel.set_value(frame)
            pixel.print_value()

    @classmethod
    def instance(cls, window: Window = None):
        if cls._instance is None:
            if window is None:
                raise WindowMissingError
            cls._instance = cls(window)
        return cls._instance
