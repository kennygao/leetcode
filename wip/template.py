from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def solution(self, ns: List[int]) -> int:
        return solve(ns)


def solve(ns: List[int]) -> int:
    return sum(ns)


def test():
    assert Solution().solution(list(range(10))) == 45
    assert Solution().solution(list(range(100))) == 4950


if __name__ == "__main__":
    test()
