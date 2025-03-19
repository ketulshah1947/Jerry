import unittest

from src.IntensitySegmentsImpl import IntensitySegments, IntensitySegmentsImpl


class TestIntensitySegments(unittest.TestCase):

    def test_set_1(self):
        segments: IntensitySegments = IntensitySegmentsImpl()
        self.assertEqual(segments.toString(), [])
        segments.add(10, 30, 1)
        self.assertEqual(segments.toString(), [[10, 1], [30, 0]])
        segments.add(20, 40, 1)
        self.assertEqual(segments.toString(), [[10, 1], [20, 2], [30, 1], [40, 0]])
        segments.add(10, 40, -2)
        self.assertEqual(segments.toString(), [[10, -1], [20, 0], [30, -1], [40, 0]])

    def test_set_2(self):
        segments: IntensitySegments = IntensitySegmentsImpl()
        self.assertEqual(segments.toString(), [])
        segments.add(10, 30, 1)
        self.assertEqual(segments.toString(), [[10, 1], [30, 0]])
        segments.add(20, 40, 1)
        self.assertEqual(segments.toString(), [[10, 1], [20, 2], [30, 1], [40, 0]])
        segments.add(10, 40, -1)
        self.assertEqual(segments.toString(), [[20, 1], [30, 0]])
        segments.add(10, 40, -1)
        self.assertEqual(segments.toString(), [[10, -1], [20, 0], [30, -1], [40, 0]])

    def test_set_no_change(self):
        segments: IntensitySegments = IntensitySegmentsImpl()
        self.assertEqual(segments.toString(), [])
        segments.add(10, 30, 2)
        self.assertEqual(segments.toString(), [[10, 2], [30, 0]])
        segments.set(10, 30, 2)
        self.assertEqual(segments.toString(), [[10, 2], [30, 0]])

    def test_set_1(self):
        segments: IntensitySegments = IntensitySegmentsImpl()
        self.assertEqual(segments.toString(), [])
        segments.add(10, 30, 2)
        self.assertEqual(segments.toString(), [[10, 2], [30, 0]])
        segments.add(20, 40, 1)
        self.assertEqual(segments.toString(), [[10, 2], [20, 3], [30, 1], [40, 0]])
        segments.set(15, 35, 5)
        self.assertEqual(segments.toString(), [[10, 2], [15, 5], [35, 1], [40, 0]])

    def test_set_2(self):
        segments: IntensitySegments = IntensitySegmentsImpl()
        self.assertEqual(segments.toString(), [])
        segments.add(10, 30, 2)
        self.assertEqual(segments.toString(), [[10, 2], [30, 0]])
        segments.add(20, 40, 1)
        self.assertEqual(segments.toString(), [[10, 2], [20, 3], [30, 1], [40, 0]])
        segments.set(10, 40, 0)
        self.assertEqual(segments.toString(), [])

    def test_set_2(self):
        segments: IntensitySegments = IntensitySegmentsImpl()
        self.assertEqual(segments.toString(), [])
        segments.add(10, 30, 1)
        self.assertEqual(segments.toString(), [[10, 1], [30, 0]])
        segments.add(20, 40, 1)
        self.assertEqual(segments.toString(), [[10, 1], [20, 2], [30, 1], [40, 0]])
        segments.set(20, 40, 3)
        self.assertEqual(segments.toString(), [[10, 1], [20, 3], [40, 0]])

    def test_set_1(self):
        segments: IntensitySegments = IntensitySegmentsImpl()
        self.assertEqual(segments.toString(), [])
        segments.add(10, 30, 1)
        self.assertEqual(segments.toString(), [[10, 1], [30, 0]])
        segments.add(20, 40, 1)
        self.assertEqual(segments.toString(), [[10, 1], [20, 2], [30, 1], [40, 0]])
        segments.set(10, 40, 2)
        self.assertEqual(segments.toString(), [[10, 2], [40, 0]])
