import heapq
from collections import Counter
from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return least_interval(tasks, n)


def least_interval(tasks, n):
    time = 0
    # negate count because heapq is a min-heap
    task_heap = [(-count, task, time) for task, count in Counter(tasks).most_common()]
    cooldown_queue = []

    while task_heap or cooldown_queue:
        time += 1
        while cooldown_queue and time - n > cooldown_queue[0][2]:
            heapq.heappush(task_heap, cooldown_queue.pop())

        if task_heap:
            count, task, _ = heapq.heappop(task_heap)
            if count + 1 < 0:
                cooldown_queue.append((count + 1, task, time))

    return time


def test():
    assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6


if __name__ == "__main__":
    test()
