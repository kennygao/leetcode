import itertools
from typing import List

from lib.treenode import TreeNode


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        return vertical_traversal(root)


def vertical_traversal(root: TreeNode) -> List[List[int]]:
    def node_x(n):
        x, y, value = n
        return x

    def node_value(n):
        x, y, value = n
        return value

    sorted_by_position = sorted(positions(root, x=0, y=0))

    grouped_by_position = [
        [node_value(n) for n in g]
        for _, g in itertools.groupby(sorted_by_position, key=node_x)
    ]

    return grouped_by_position


def positions(root, x, y):
    if root is None:
        return []
    return (
        positions(root.left, x - 1, y + 1)
        + [(x, y, root.val)]
        + positions(root.right, x + 1, y + 1)
    )


def test():
    n = TreeNode

    # example 1
    assert Solution().verticalTraversal(n(3, n(9), n(20, n(15), n(7)))) == [
        [9],
        [3, 15],
        [20],
        [7],
    ]

    # example 2
    assert Solution().verticalTraversal(n(1, n(2, n(4), n(5)), n(3, n(6), n(7)))) == [
        [4],
        [2],
        [1, 5, 6],
        [3],
        [7],
    ]

    # full 4-level tree
    assert Solution().verticalTraversal(
        n(
            1,
            n(2, n(4, n(8), n(9)), n(5, n(10), n(11))),
            n(3, n(6, n(12), n(13)), n(7, n(14), n(15))),
        )
    ) == [[8], [4], [2, 9, 10, 12], [1, 5, 6], [3, 11, 13, 14], [7], [15]]

    # level order example (9 > 7)
    assert Solution().verticalTraversal(
        n(0, n(5, n(9)), n(1, n(2, None, n(3, n(4, n(6, n(7))), n(8)))))
    ) == [[9, 7], [5, 6], [0, 2, 4], [1, 3], [8]]


if __name__ == "__main__":
    test()
