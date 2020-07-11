import itertools
from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def subsets(self, ns: List[int]) -> List[List[int]]:
        return solve(ns)


def solve(ns: List[int]) -> List[List[int]]:
    return [
        list(subset)
        for i in range(len(ns) + 1)
        for subset in itertools.combinations(ns, i)
    ]


def test():
    assert Solution().subsets([1, 2, 3]) == [
        [],
        [1],
        [2],
        [3],
        [1, 2],
        [1, 3],
        [2, 3],
        [1, 2, 3],
    ]


if __name__ == "__main__":
    test()
