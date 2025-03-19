from abc import abstractmethod


class IntensitySegments:
    @abstractmethod
    def add(self, from_idx: int, to_idx: int, amount: int):
        pass

    @abstractmethod
    def set(self, from_idx: int, to_idx: int, amount: int):
        pass

    @abstractmethod
    def toString(self):
        pass
