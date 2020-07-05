class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def hammingDistance(self, x: int, y: int) -> int:
        return solve(x, y)


def solve(x: int, y: int) -> int:
    return sum(int(b) for b in format(x ^ y, "b"))


def test():
    assert Solution().hammingDistance(1, 4) == 2


if __name__ == "__main__":
    test()
