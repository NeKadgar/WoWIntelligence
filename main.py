from screen.video_window import VideoWindow
from screen.display import Display, DisplayType
from screen.window_stream import WindowStream
from game.game_info import GameInfo
from vision.feature_extractor import FeatureExtractor

window = VideoWindow("warcraft_sample")
info = GameInfo.instance(window)
display = Display(window.width, window.height, DisplayType.RGB)
extractor = FeatureExtractor()

for frame in WindowStream(window).get_stream():
    info.update(frame)
    matches = extractor.extract_matches(frame)
    display.paint(frame.draw_matches_lines(matches))
