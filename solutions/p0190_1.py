class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def reverseBits(self, n: int) -> int:
        return solve(n)


def solve(n: int) -> int:
    return int("".join(reversed(format(n, "b").zfill(32))), 2)


def test():
    assert Solution().reverseBits(43261596) == 964176192
    assert Solution().reverseBits(4294967293) == 3221225471


if __name__ == "__main__":
    test()
