from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def solve(self, ns: List[int]) -> int:
        return solution(ns)


def solution(ns: List[int]):
    return sum(ns)


def test():
    assert Solution().solve(list(range(10))) == 45
    assert Solution().solve(list(range(100))) == 4950


if __name__ == "__main__":
    test()
