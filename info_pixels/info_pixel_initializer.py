from typing import Dict
from enum import Enum, auto
from info_pixels.game_info_pixel import GameInfoPixel
import matplotlib.pyplot as plt

from screen.frame import Frame


class InfoPixelInitializerStatus(Enum):
    EXIT = auto()
    CONTINUE = auto()
    ALMOST_GOODBYE = auto()


class InfoPixelInitializer:
    SET_POS = 'x'
    BACK = 'z'

    def __init__(self, frame: Frame, pixels_dict: Dict[str, GameInfoPixel]):
        self._step = 0
        self.sensors: dict = pixels_dict
        self._current_status = InfoPixelInitializerStatus.CONTINUE

        self._fig, self._ax = plt.subplots()

        self.help_text = plt.text(1, 1, self._get_current_text(), ha='right', transform=self._ax.transAxes, fontsize=20,
                                  wrap=True)
        self.help_text.set_bbox(dict(facecolor='red', alpha=0.5, edgecolor='red'))

        self.sensors_text = plt.text(1, 0, "", ha='right', transform=self._ax.transAxes, fontsize=20, wrap=True)
        self.sensors_text.set_bbox(dict(facecolor='yellow', alpha=0.5, edgecolor='yellow'))

        self._ax.imshow(frame.image)
        self._fig.canvas.mpl_connect('key_press_event', self._on_press)
        plt.show()

    def _on_press(self, event):
        if event.key == self.SET_POS:
            self._on_set_pos(int(event.xdata), int(event.ydata))
            self._step += 1
        elif event.key == self.BACK:
            self._step -= 1
        self._update_status()
        if self._current_status == InfoPixelInitializerStatus.EXIT:
            plt.close()
            return
        self.help_text.set_text(self._get_current_text())
        self.sensors_text.set_text(self._get_sensors_text())
        plt.pause(0)

    def _on_set_pos(self, x: int, y: int):
        keys = list(self.sensors.keys())
        if len(keys) > self._step:
            sensor_name = self._get_current_sensor_name()
            sensor = self.sensors.get(sensor_name)
            if isinstance(sensor, type):
                self.sensors[sensor_name] = sensor(sensor_name, x, y)
            else:
                self.sensors[sensor_name].set_position(x, y)

    def _update_status(self):
        if self._step == -1:
            self._current_status = InfoPixelInitializerStatus.EXIT
            return
        keys_length = len(self.sensors.keys())
        if self._step == keys_length:
            self._current_status = InfoPixelInitializerStatus.ALMOST_GOODBYE
            return
        if self._step > keys_length:
            self._current_status = InfoPixelInitializerStatus.EXIT
            return
        self._current_status = InfoPixelInitializerStatus.CONTINUE
        return

    def _get_current_text(self):
        if self._current_status == InfoPixelInitializerStatus.ALMOST_GOODBYE:
            return f"To exit press {self.SET_POS.upper()} again"
        sensor_name = self._get_current_sensor_name()
        return f"{sensor_name} sensor:\npress {self.SET_POS.upper()} - to set position\npress {self.BACK.upper()} - to return"

    def _get_current_sensor_name(self):
        return list(self.sensors.keys())[self._step]

    def _get_sensors_text(self):
        text = ""
        for key, sensor in self.sensors.items():
            if not isinstance(sensor, type):
                text += f"{key.upper()} - {sensor.x} {sensor.y}\n"
        return text
