from typing import List


class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def plusOne(self, digits: List[int]) -> List[int]:
        return solve_1(digits)


def solve_1(digits: List[int]) -> List[int]:
    return list(map(int, str(1 + int("".join(map(str, digits))))))


def solve_2(digits: List[int]) -> List[int]:
    return list(
        map(
            int,
            str(1 + sum(digit * (10 ** p) for p, digit in enumerate(reversed(digits)))),
        )
    )


def solve_3(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits


def test():
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]


if __name__ == "__main__":
    test()
