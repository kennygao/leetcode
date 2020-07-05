import heapq


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def nthUglyNumber(self, n: int) -> int:
        return solve(n)


def solve(n: int) -> int:
    heap = [1]
    seen = {1}

    for _ in range(n - 1):
        x = heapq.heappop(heap)
        for factor in (2, 3, 5):
            if (candidate := factor * x) not in seen:
                heapq.heappush(heap, candidate)
                seen.add(candidate)

    return heapq.heappop(heap)


def test():
    assert Solution().nthUglyNumber(10) == 12


if __name__ == "__main__":
    test()
