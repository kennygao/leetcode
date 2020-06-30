import itertools
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        return exclusive_time(n, logs)


def exclusive_time(n: int, logs: List[str]) -> List[int]:
    def compute_function_time(segment):
        left, right = segment
        if left[1] == "start" and right[1] == "start":
            return left[0], int(right[2]) - int(left[2])
        if left[1] == "start" and right[1] == "end":
            return left[0], int(right[2]) - int(left[2]) + 1
        if left[1] == "end" and right[1] == "start":
            # Apparently, this is legal input.
            raise Exception
        if left[1] == "end" and right[1] == "end":
            return right[0], int(right[2]) - int(left[2])

    parsed_logs = [log.split(":") for log in logs]
    print(f"{parsed_logs=}")

    segments = list(zip(parsed_logs[:-1], parsed_logs[1:]))
    print(f"{segments=}")

    segment_time = [compute_function_time(segment) for segment in segments]
    print(f"{segment_time=}")

    segment_time_sorted_by_id = sorted(segment_time, key=lambda time: time[0])
    print(f"{segment_time_sorted_by_id=}")

    segment_time_summed_by_id = [
        (k, sum(time[1] for time in g))
        for k, g in itertools.groupby(
            segment_time_sorted_by_id, key=lambda time: time[0]
        )
    ]
    print(f"{segment_time_summed_by_id=}")

    result = [time for function, time in segment_time_summed_by_id]
    print(f"{result=}")

    return result


def test():
    assert Solution().exclusiveTime(
        2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    ) == [3, 4]


if __name__ == "__main__":
    test()
