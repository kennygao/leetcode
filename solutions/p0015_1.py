import itertools
from collections import Counter
from typing import Iterable, List, TypeVar


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def threeSum(self, ns: List[int]) -> List[List[int]]:
        return solve_3(ns)


def solve_1(ns: List[int]) -> List[List[int]]:
    ns.sort()
    combinations = [
        list(combination)
        for combination in itertools.combinations(ns, 3)
        if sum(combination) == 0
    ]
    return unique(combinations)


T = TypeVar("T")


def unique(ts: Iterable[T]) -> List[T]:
    return [k for k, _ in itertools.groupby(sorted(ts))]


def solve_2(ns: List[int]) -> List[List[int]]:
    counter = Counter(ns)
    combinations = {
        (a, b, c)
        for a in counter
        for b in counter - Counter({a: 1})
        if (c := -(a + b)) in counter - Counter({a: 1}) - Counter({b: 1})
        if a <= b <= c
    }
    return [list(combination) for combination in combinations]


def solve_3(ns: List[int]) -> List[List[int]]:
    ns.sort()

    results = set()

    for i in range(len(ns) - 2):
        l, r = i + 1, len(ns) - 1

        while l < r:
            candidate = ns[l] + ns[r]
            if candidate < -ns[i]:
                l += 1
            elif candidate > -ns[i]:
                r -= 1
            else:
                results.add((ns[i], ns[l], ns[r]))
                l += 1
                r -= 1

    return [list(result) for result in results]


def test():
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]


if __name__ == "__main__":
    test()
