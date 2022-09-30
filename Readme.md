# World of Warcraft Vision

## Examples:

### Create video:
```python
from screen.mss_window import MSSWindow
from screen.window_stream import WindowStream
from screen.recorder.frame_queue import FrameQueue
from screen.recorder.video_recorder import VideoRecorder


# initialize any window
window = MSSWindow(0, 0, 1920, 1080)

# initialize queue of frames
queue = FrameQueue()

# start streaming window
for frame in WindowStream(window).get_stream():
    # add frame
    queue.add(frame)

# Create video file "wow_sample.avi"
VideoRecorder.create_video_from_queue(queue, "wow_sample", fps=120)
```