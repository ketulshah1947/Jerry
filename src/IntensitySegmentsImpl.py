from functools import cmp_to_key
from sortedcontainers import SortedDict

from src.IntensitySegments import IntensitySegments


class IntensitySegmentsImpl(IntensitySegments):
    segments: SortedDict[int, int]

    def __init__(self):
        self.segments = SortedDict()

    def add(self, from_idx: int, to_idx: int, amount: int):
        self._update_segment(from_idx, amount)
        self._update_segment(to_idx, -amount)

    def set(self, from_idx: int, to_idx: int, amount: int):
        current_intensity = 0
        if from_idx not in self.segments:
            self._update_segment(from_idx, 0)
        if to_idx not in self.segments:
            self._update_segment(to_idx, 0)
        segments = list(self.segments.items())
        print(self.segments)
        print(segments)
        for position, change in segments:
            if position < from_idx:
                current_intensity += change
            elif position == from_idx:
                self.segments[position] = amount - current_intensity
                if change is not None:
                    current_intensity += change
            elif position > from_idx and position < to_idx:
                current_intensity += change
                self.segments.pop(position)
            elif position == to_idx:
                if change is not None:
                    current_intensity += change
                self.segments[position] = current_intensity - amount

    def toString(self):
        result = []
        current_intensity = 0
        for position, change in self.segments.items():
            current_intensity += change
            if current_intensity != 0 or len(result) != 0:
                result.append([position, current_intensity])
        while len(result) > 1 and result[-1][1] == 0 and result[-2][1] == 0:
            result.pop(-1)
        return result

    def _update_segment(self, position: int, amount: int):
        if position not in self.segments:
            self.segments[position] = amount
        else:
            self.segments[position] = self.segments[position] + amount
