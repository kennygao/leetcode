from typing import Dict, Iterable, List, Mapping

from lib.treenode import TreeNode


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return solve(root)


def solve(root: TreeNode) -> List[List[int]]:
    values_by_level = traversal(root, level=0)
    return [values_by_level[k] for k in sorted(values_by_level.keys(), reverse=True)]


def traversal(root: TreeNode, level: int) -> Dict[int, List[int]]:
    if root:
        return merge(
            {level: [root.val]},
            traversal(root.left, level + 1),
            traversal(root.right, level + 1),
        )
    else:
        return {}


def merge(*dicts: Mapping[int, Iterable[int]]) -> Dict[int, List[int]]:
    return {
        k: [v for d in dicts for v in d.get(k, [])]
        for k in {k for d in dicts for k in d.keys()}
    }


def test():
    # test merge
    assert merge(
        {1: [1, 2], 2: [1, 2]}, {2: [2, 3], 3: [2, 3]}, {3: [3, 4], 4: [3, 4]}
    ) == {1: [1, 2], 2: [1, 2, 2, 3], 3: [2, 3, 3, 4], 4: [3, 4]}

    # test traversal
    n = TreeNode

    # example 1
    example_1 = n(3, n(9), n(20, n(15), n(7)))
    assert traversal(example_1, level=0) == {0: [3], 1: [9, 20], 2: [15, 7]}
    assert Solution().levelOrderBottom(example_1) == [[15, 7], [9, 20], [3]]


if __name__ == "__main__":
    test()
