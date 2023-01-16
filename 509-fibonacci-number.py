class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        lst = [0, 1]
        for i in range(2, n + 1):
            lst.append(lst[-1] + lst[-2])

        return lst[-1]