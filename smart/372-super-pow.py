from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def myPow(x, n):
            r = 1
            for i in range(n):
                r *= x
                r %= 1337

            return r

        rs = 1
        for i in range(len(b)):
            r = myPow(a, b[i])
            rs *= r
            rs %= 1337

            if i != len(b) - 1:
                rs = myPow(rs, 10)

        return rs