import collections
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        return exclusive_time(n, logs)


def exclusive_time(n: int, logs: List[str]) -> List[int]:
    stack = []
    time = collections.defaultdict(int)

    for log in logs:
        function_id, status, timestamp = log.split(":")
        function_id = int(function_id)
        timestamp = int(timestamp)

        if not stack:
            stack.append((function_id, timestamp))
        else:
            if status == "start":
                last_function_id, last_timestamp = stack[-1]
                time[last_function_id] += timestamp - last_timestamp
                stack.append((function_id, timestamp))
            if status == "end":
                last_function_id, last_timestamp = stack.pop()
                time[function_id] += timestamp - last_timestamp + 1
                if stack:
                    current_function_id, _ = stack.pop()
                    stack.append((current_function_id, timestamp + 1))

    output = [function_time for function_id, function_time in sorted(time.items())]
    return output


def test():
    assert Solution().exclusiveTime(
        2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    ) == [3, 4]


if __name__ == "__main__":
    test()
