import time
from mss import mss
from screen.mss_window import MSSWindow
from screen.display import Display
from screen.wow_stream import WindowStream
from game.game_info import GameInfo


monitor = mss().monitors[0]
display = Display(monitor.get("width"), monitor.get("height"))
window = MSSWindow(**monitor)
info = GameInfo.instance()

for image in WindowStream(window).get_stream():
    t = time.time()
    display.paint(image)
    print(time.time() - t)
