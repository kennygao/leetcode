from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def twoSum(self, ns: List[int], target: int) -> List[int]:
        return solve(ns, target)


def solve(ns: List[int], target: int) -> List[int]:
    sorted_ns = list(sorted(enumerate(ns), key=lambda x: x[1]))

    l, r = 0, len(sorted_ns) - 1

    while l < r:
        candidate = sorted_ns[l][1] + sorted_ns[r][1]
        if candidate < target:
            l += 1
        elif candidate > target:
            r -= 1
        else:
            return [sorted_ns[l][0], sorted_ns[r][0]]

    return []


def test():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


if __name__ == "__main__":
    test()
