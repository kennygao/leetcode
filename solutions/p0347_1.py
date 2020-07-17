from collections import Counter
from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def topKFrequent(self, ns: List[int], k: int) -> List[int]:
        return solve(ns, k)


def solve(ns: List[int], k: int) -> List[int]:
    return [n for n, _ in Counter(ns).most_common(k)]


def test():
    assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert Solution().topKFrequent([1], 1) == [1]


if __name__ == "__main__":
    test()
