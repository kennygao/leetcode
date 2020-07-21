from typing import List, Mapping


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        return solve(n, edges)


def solve(n: int, edges: List[List[int]]) -> List[int]:
    vertex = int
    parent, child = vertex, vertex

    constraints: Mapping[parent, List[child]] = {v: [] for v in range(n)}
    indegree: Mapping[vertex, int] = {v: 0 for v in range(n)}

    for c, p in edges:
        constraints[p].append(c)
        indegree[c] += 1

    free = [v for v, degree in indegree.items() if not degree]

    order = []

    while free:
        v = free.pop()
        order.append(v)
        for c in constraints[v]:
            indegree[c] -= 1
            if not indegree[c]:
                free.append(c)

    return order if len(order) == n else []


def test():
    assert Solution().findOrder(0, []) == []
    assert Solution().findOrder(1, []) == [0]
    assert Solution().findOrder(1, [[0, 0]]) == []

    # example 1
    assert Solution().findOrder(2, [[1, 0]]) == [0, 1]

    # example 2
    assert Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in (
        [0, 1, 2, 3],
        [0, 2, 1, 3],
    )


if __name__ == "__main__":
    test()
