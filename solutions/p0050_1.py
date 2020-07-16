import math


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def myPow(self, base: float, power: int) -> float:
        return solve(base, power)


def solve(base: float, power: int) -> float:
    if power == 0:
        return 1

    if power == 1:
        return base

    if power < 0:
        return 1 / solve(base, -power)

    a = solve(base, power // 2)
    b = solve(base, power % 2)
    return a * a * b


def test():
    assert math.isclose(Solution().myPow(2, 0), 1)
    assert math.isclose(Solution().myPow(2, 1), 2)
    assert math.isclose(Solution().myPow(2, -1), 0.5)

    assert math.isclose(Solution().myPow(-1, 2 ** 31 - 1), -1)

    assert math.isclose(Solution().myPow(2, 10), 1024)
    assert math.isclose(Solution().myPow(2.1, 3), 9.261)
    assert math.isclose(Solution().myPow(2, -2), 0.25)


if __name__ == "__main__":
    test()
