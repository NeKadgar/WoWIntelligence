import cv2
import numpy

from screen.frame import Frame
from application_types import PixelsArray


class FeatureExtractor:
    def __init__(self):
        self._extractor = cv2.ORB_create(100000)  # noqa, can be SIFT
        self._matcher = cv2.BFMatcher(cv2.NORM_HAMMING)  # noqa
        self.last = None

    def extract_matches(self, frame: Frame):
        kps, des = self.extract_features(frame)
        matches = self._get_matches(des)
        matches = self._sort_matches(matches)
        matches = self._convert_to_points(kps, matches)
        self.last = {'kps': kps, 'des': des}
        return matches

    @staticmethod
    def _sort_matches(matches):
        def sort_by_distance(match):
            m, n = match
            return m.distance < 0.55*n.distance
        return filter(sort_by_distance, matches)

    def _convert_to_points(self, kps, matches):
        ret = []
        for m, n in matches:
            ret.append((kps[m.queryIdx], self.last['kps'][m.trainIdx]))
        return ret

    def extract_features(self, frame: Frame):
        gray_img = frame.get_grayscale()
        pts = cv2.goodFeaturesToTrack(
            gray_img,
            300000,
            qualityLevel=0.001,
            minDistance=10,
            # useHarrisDetector=True,
            # k=0.000001
        )
        # if pts is None:
        #     pts = []

        # extraction
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in pts]
        kps, des = self._extractor.compute(gray_img, kps)
        return kps, des

    def _get_matches(self, des):
        # if self.last is None or des is None or self.last['des'] is None:
        #     return []
        if self.last is None:
            return []

        matches = self._matcher.knnMatch(des, self.last['des'], k=2)
        return matches
