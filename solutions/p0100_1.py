from lib.treenode import TreeNode


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return solve(p, q)


def solve(p: TreeNode, q: TreeNode) -> bool:
    return (not p and not q) or (
        (p and q)
        and p.val == q.val
        and solve(p.left, q.left)
        and solve(p.right, q.right)
    )


def test():
    n = TreeNode

    # example 1
    assert Solution().isSameTree(n(1, n(2), n(3)), n(1, n(2), n(3)))

    # example 2
    assert not Solution().isSameTree(n(1, n(2), None), n(1, None, n(2)))

    # example 3
    assert not Solution().isSameTree(n(1, n(2), n(1)), n(1, n(1), n(2)))


if __name__ == "__main__":
    test()
