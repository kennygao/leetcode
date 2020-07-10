import itertools
from typing import Sequence

from lib.treenode import TreeNode


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return solve(root)


def solve(root: TreeNode) -> int:
    level = [root]
    max_width = len(level)

    while level:
        level = trim_ends(
            list(
                itertools.chain.from_iterable(
                    (
                        (node.left, node.right) if node else (None, None)
                        for node in level
                    )
                )
            )
        )
        max_width = max(max_width, len(level))

    return max_width


def trim_ends(sequence: Sequence) -> Sequence:
    l, r = 0, len(sequence)

    while l < r and not sequence[l]:
        l += 1

    while l < r and not sequence[r - 1]:
        r -= 1

    return sequence[l:r]


def test():
    # test trim_ends
    assert trim_ends([None, 1, 1, 1, None, None, None]) == [1, 1, 1]

    # test solve
    n = TreeNode

    assert Solution().widthOfBinaryTree(n(0)) == 1

    # example 1
    example_1 = n(1, n(3, n(5), n(3)), n(2, None, n(9)))
    assert Solution().widthOfBinaryTree(example_1) == 4


if __name__ == "__main__":
    test()
