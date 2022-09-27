import time
import cv2

from screen.mss_window import MSSWindow
from screen.display import Display, DisplayType
from screen.wow_stream import WindowStream
from game.game_info import GameInfo
from vision.feature_extractor import FeatureExtractor

window = MSSWindow.from_dragged_zone()
display = Display(window.width, window.height, DisplayType.RGB)
info = GameInfo.instance(window)
extractor = FeatureExtractor()


for image in WindowStream(window).get_stream():
    t = time.time()
    info.update(image)
    matches = extractor.extract_matches(image)

    # draw matching lines
    if matches is not None:
        for p1, p2 in matches:
            u1, v1 = map(lambda x: int(round(x)), p1.pt)
            u2, v2 = map(lambda x: int(round(x)), p2.pt)
            image = cv2.line(image, (u1, v1), (u2, v2), (0, 0, 255), 2)
        print(f"{len(matches)} matches")

    display.paint(image)
    print(f"{1.0 / (time.time() - t) :,.2f} fps")
