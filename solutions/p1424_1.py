from typing import Any, List, NamedTuple, Tuple


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def findDiagonalOrder(self, ns: List[List[int]]) -> List[int]:
        return solve(ns)


def solve(ns: List[List[int]]) -> List[int]:
    lane_count = max(i + len(row) for i, row in enumerate(ns))
    lanes = [[] for _ in range(lane_count)]

    for r, row in reversed(list(enumerate(ns))):
        for c, n in enumerate(row):
            lanes[r + c].append(n)

    traversal = [n for lane in lanes for n in lane]
    return traversal


class TestCase(NamedTuple):
    arguments: Tuple[Any, ...]
    expectation: Any


def test():
    test_cases = [
        TestCase(
            arguments=([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
            expectation=[1, 4, 2, 7, 5, 3, 8, 6, 9],
        ),
        TestCase(
            arguments=(
                [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]],
            ),
            expectation=[1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16],
        ),
        TestCase(
            arguments=([[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]],),
            expectation=[1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11],
        ),
        TestCase(arguments=([[1, 2, 3, 4, 5, 6]],), expectation=[1, 2, 3, 4, 5, 6]),
    ]

    for arguments, expectation in test_cases:
        assert Solution().findDiagonalOrder(*arguments) == expectation


if __name__ == "__main__":
    test()
