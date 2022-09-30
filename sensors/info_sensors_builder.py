from typing import Dict
from enum import Enum, auto
import matplotlib.pyplot as plt

from screen.frame import Frame
from sensors.base_info_sensor import BaseInfoSensor


class InfoSensorsBuilderStatus(Enum):
    EXIT = auto()
    CONTINUE = auto()
    ALMOST_GOODBYE = auto()


class InfoSensorsBuilder:
    SET_POS = 'x'
    BACK = 'z'

    @classmethod
    def from_sensors_dict(cls, frame: Frame, sensors_dict: Dict[str, BaseInfoSensor]):
        builder = cls(frame, sensors_dict)
        return builder._sensors

    def __init__(self, frame: Frame, sensors_dict: Dict[str, BaseInfoSensor]):
        self._step = 0
        self._sensors_schema: dict = sensors_dict
        self._sensors = dict()
        self._current_status = InfoSensorsBuilderStatus.CONTINUE

        self._fig, self._ax = plt.subplots()

        self.help_text = plt.text(1, 1, self._get_current_text(), ha='right', transform=self._ax.transAxes, fontsize=20,
                                  wrap=True)
        self.help_text.set_bbox(dict(facecolor='red', alpha=0.5, edgecolor='red'))

        self.sensors_text = plt.text(1, 0, "", ha='right', transform=self._ax.transAxes, fontsize=20, wrap=True)
        self.sensors_text.set_bbox(dict(facecolor='yellow', alpha=0.5, edgecolor='yellow'))
        self._frame = frame
        self._im = self._ax.imshow(self._frame.get_matplot_format())
        self._fig.canvas.mpl_connect('key_press_event', self._on_press)
        plt.show()

    def _on_press(self, event):
        if event.key == self.SET_POS:
            self._on_set_pos(int(event.xdata), int(event.ydata))
            self._step += 1
        elif event.key == self.BACK:
            self._step -= 1
        self._update_status()
        if self._current_status == InfoSensorsBuilderStatus.EXIT:
            plt.close()
            return
        self.help_text.set_text(self._get_current_text())
        self._update_sensors_visible_info()
        plt.pause(0)

    def _on_set_pos(self, x: int, y: int):
        keys = list(self._sensors_schema.keys())
        if len(keys) > self._step:
            sensor_name = self._get_current_sensor_name()
            sensor = self._sensors_schema.get(sensor_name)
            if isinstance(sensor, type):
                self._sensors[sensor_name] = sensor(sensor_name, x, y)
            else:
                self._sensors[sensor_name].set_position(x, y)

    def _update_status(self):
        if self._step == -1:
            self._current_status = InfoSensorsBuilderStatus.EXIT
            return
        keys_length = len(self._sensors_schema.keys())
        if self._step == keys_length:
            self._current_status = InfoSensorsBuilderStatus.ALMOST_GOODBYE
            return
        if self._step > keys_length:
            self._current_status = InfoSensorsBuilderStatus.EXIT
            return
        self._current_status = InfoSensorsBuilderStatus.CONTINUE
        return

    def _get_current_text(self):
        if self._current_status == InfoSensorsBuilderStatus.ALMOST_GOODBYE:
            return f"To exit press {self.SET_POS.upper()} again"
        sensor_name = self._get_current_sensor_name()
        return f"{sensor_name} sensor:\npress {self.SET_POS.upper()} - to set position\npress {self.BACK.upper()} - to return"

    def _get_current_sensor_name(self):
        return list(self._sensors_schema.keys())[self._step]

    def _update_sensors_visible_info(self):
        self.sensors_text.set_text(self._get_sensors_text())
        self._show_circles()

    def _show_circles(self):
        circles = []
        for sensor in self._sensors.values():
            circles.append((sensor.x, sensor.y))
        self._im.set_data(self._frame.matplot_draw_circles(circles))

    def _get_sensors_text(self):
        text = ""
        for key, sensor in self._sensors.items():
            text += f"{key.upper()} - {sensor.x} {sensor.y}\n"
        return text
