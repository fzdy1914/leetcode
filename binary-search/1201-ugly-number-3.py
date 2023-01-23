import math


class Solution:
    # TODO: math.gcd ???
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = a * bc // math.gcd(a, bc)

        def calc(n):
            return n // a + n // b + n // c - n // ab - n // ac - n // bc + n // abc

        start = 1
        end = 2 * 10 ** 9

        while start + 1 < end:
            mid = start + (end - start) // 2

            t = calc(mid)
            if t >= n:
                end = mid
            else:
                start = mid

        if calc(start) == n and (start % a == 0 or start % b == 0 or start % c == 0):
            return start

        return end