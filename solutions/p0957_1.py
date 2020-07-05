from typing import List, Tuple


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        return solve(cells, n)


Cells = List[int]


def solve(cells: Cells, n: int) -> Cells:
    history: List[Cells] = []

    while (cells := tick(cells)) not in history:
        history.append(cells)

    period = len(history) - history.index(cells)

    return history[n % period - 1]


def tick(cells: Cells) -> Cells:
    l_neighbors = cells[:-2]
    r_neighbors = cells[2:]
    neighborhoods = zip(l_neighbors, r_neighbors)
    return [0, *(tick_cell(neighborhood) for neighborhood in neighborhoods), 0]


def tick_cell(neighborhood: Tuple[int, int]) -> int:
    left, right = neighborhood
    return 1 if left == right else 0


def test():
    assert Solution().prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7) == [
        0,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
    ]
    assert Solution().prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 10 ** 9) == [
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        0,
    ]


if __name__ == "__main__":
    test()
