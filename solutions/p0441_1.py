import math


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def arrangeCoins(self, n: int) -> int:
        return solve(n)


def solve(n: int) -> int:
    assert n >= 0

    return math.floor(triangular_root(n))


def triangular_root(n: float) -> float:
    return (math.sqrt(8 * n + 1) - 1) / 2


def test():
    assert Solution().arrangeCoins(0) == 0
    assert Solution().arrangeCoins(1) == 1
    assert Solution().arrangeCoins(2) == 1
    assert Solution().arrangeCoins(3) == 2
    assert Solution().arrangeCoins(5) == 2
    assert Solution().arrangeCoins(8) == 3


if __name__ == "__main__":
    test()
