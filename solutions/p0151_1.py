class Solution:
    # noinspection PyMethodMayBeStatic
    # noinspection PyPep8Naming
    def reverseWords(self, s: str) -> str:
        return solve(s)


def solve(s: str) -> str:
    return " ".join(reversed(s.split()))


def test():
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"
    assert Solution().reverseWords("  hello world!  ") == "world! hello"
    assert Solution().reverseWords("a good   example") == "example good a"


if __name__ == "__main__":
    test()
