from typing import Optional


class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def flatten(self, root: Node) -> Node:
        return solve(root)


def solve(root: Node) -> Optional[Node]:
    if not root:
        return None

    head = root
    stack = []

    while head.child or head.next or stack:
        if head.child:
            if head.next:
                stack.append(head.next)
            head.next = head.child
            head.next.prev = head
            head.child = None
        if not head.next and stack:
            head.next = stack.pop()
            head.next.prev = head
        head = head.next

    return root


def test():
    def values(node):
        while node:
            yield node
            node = node.next

    # example 2
    n1, n2, n3 = Node(1), Node(2), Node(3)
    n1.next = n2
    n2.prev = n1
    n1.child = n3
    assert [node.val for node in values(Solution().flatten(n1))] == [1, 3, 2]


if __name__ == "__main__":
    test()
