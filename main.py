import time

from screen.mss_window import MSSWindow
from screen.display import Display
from screen.wow_stream import WindowStream
from game.game_info import GameInfo


window = MSSWindow.from_dragged_zone()
display = Display(window.width, window.height)
info = GameInfo.instance(window)

for image in WindowStream(window).get_stream():
    t = time.time()
    display.paint(image)
    print(time.time() - t)
