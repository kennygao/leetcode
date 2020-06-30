from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return solve(temperatures)


def solve(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    distances = [0] * n

    for i in range(n - 1, -1, -1):
        distances[i] = days_until_higher_temperature(
            temperatures[i], temperatures, distances, i + 1
        )

    return distances


def days_until_higher_temperature(
    t: int, forecast: List[int], distances: List[int], i: int = 0
) -> int:
    assert len(forecast) == len(distances)

    if i >= len(forecast):
        return 0

    if forecast[i] > t:
        return 1

    skip = distances[i]

    if not skip:
        return 0

    distance_from_tomorrow = days_until_higher_temperature(
        t, forecast, distances, i + skip
    )

    return skip + distance_from_tomorrow if distance_from_tomorrow else 0


def test():
    assert days_until_higher_temperature(70, [], []) == 0
    assert days_until_higher_temperature(70, [70], [0]) == 0
    assert days_until_higher_temperature(70, [71], [0]) == 1
    assert days_until_higher_temperature(70, [70, 71], [1, 0]) == 2
    assert days_until_higher_temperature(70, [69, 70, 71], [1, 1, 0]) == 3
    assert days_until_higher_temperature(70, [69, 68, 67, 71], [3, 2, 1, 0]) == 4
    assert days_until_higher_temperature(70, [67, 68, 69, 70], [1, 1, 1, 0]) == 0

    # given example
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]


if __name__ == "__main__":
    test()
