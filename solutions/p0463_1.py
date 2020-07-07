import itertools
from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return solve(grid)


def solve(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    rows, cols = range(m), range(n)

    def perimeter(r: int, c: int) -> int:
        adjacencies = [
            r - 1 in rows and grid[r - 1][c],
            r + 1 in rows and grid[r + 1][c],
            c - 1 in cols and grid[r][c - 1],
            c + 1 in cols and grid[r][c + 1],
        ]
        return sum(1 for adjacency in adjacencies if not adjacency)

    return sum(perimeter(r, c) for r, c in itertools.product(rows, cols) if grid[r][c])


def test():
    assert (
        Solution().islandPerimeter(
            [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        )
        == 16
    )


if __name__ == "__main__":
    test()
