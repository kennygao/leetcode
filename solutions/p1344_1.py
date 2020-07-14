class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def angleClock(self, h: int, m: int) -> float:
        return solve(h, m)


def solve(h: int, m: int) -> float:
    h_angle = h * 30 + m / 2
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    return min(angle, 360 - angle)


def test():
    assert Solution().angleClock(12, 30) == 165
    assert Solution().angleClock(3, 30) == 75
    assert Solution().angleClock(3, 15) == 7.5
    assert Solution().angleClock(4, 50) == 155
    assert Solution().angleClock(12, 0) == 0


if __name__ == "__main__":
    test()
