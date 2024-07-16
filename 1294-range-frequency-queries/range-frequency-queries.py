class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = defaultdict(list)

        for i, j in enumerate(arr):
            self.arr[j].append(i)

    def query(self, left: int, right: int, value: int) -> int:

        return bisect.bisect_right(self.arr[value], right) - bisect.bisect_left(self.arr[value], left)   