import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return kth_largest(nums, k)


def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


def test():
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


if __name__ == "__main__":
    test()
