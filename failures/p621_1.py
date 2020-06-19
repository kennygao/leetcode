import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return least_interval(tasks, n)


def least_interval(tasks, n):
    counter = collections.Counter(tasks)
    long_pole, long_pole_length = counter.most_common(1)[0]
    long_pole_count = list(counter.values()).count(long_pole_length)
    return (n + 1) * (long_pole_length - 1) + long_pole_count


def test():
    assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6


if __name__ == "__main__":
    test()
