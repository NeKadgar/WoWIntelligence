import time
import keyboard

from screen.mss_window import MSSWindow
from screen.display import Display, DisplayType
from screen.window_stream import WindowStream
from screen.recorder.video_recorder import VideoRecorder
from screen.recorder.frame_queue import FrameQueue
from game.game_info import GameInfo
from vision.feature_extractor import FeatureExtractor

window = MSSWindow.from_dragged_zone()
# window = MSSWindow(0, 0, 1920, 1080)
display = Display(window.width, window.height, DisplayType.RGB)
info = GameInfo.instance(window)
extractor = FeatureExtractor()
queue = FrameQueue()

t = time.time()
record_started = False

for frame in WindowStream(window).get_stream():
    if record_started:
        queue.add(frame)

    info.update(frame)
    matches = extractor.extract_matches(frame)
    display.paint(frame.draw_matches_lines(matches))

    if keyboard.is_pressed("P"):
        record_started = True

    if keyboard.is_pressed("Q"):
        break

    print(1.0 / (time.time() - t))
    t = time.time()

VideoRecorder.create_video_from_queue(queue, "new", fps=120)
