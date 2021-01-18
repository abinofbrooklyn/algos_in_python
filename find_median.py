class MedianFinder:
    def __init__(self):
        self._stream = []

    def add_num(self, num: int) -> None:
        self._stream.append(num)

    def find_median(self) -> float:
        self._stream.sort()
        n = len(self._stream)

        if n & 1:
            return self._stream([n//2])
        else:
            return (self._stream[n//2-1] + self._stream[n//2]) * 0.5
