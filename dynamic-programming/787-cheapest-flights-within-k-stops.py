from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        reversedFlights = dict()
        for f in flights:
            if f[1] not in reversedFlights:
                reversedFlights[f[1]] = [(f[0], f[2])]
            else:
                reversedFlights[f[1]].append((f[0], f[2]))
        memo = dict()

        def helper(src, dst, k):
            if (dst, k) in memo:
                return memo[(dst, k)]

            if src == dst:
                return 0

            if k == 0:
                return float("inf")

            m = float("inf")
            if dst in reversedFlights:
                for rf in reversedFlights[dst]:
                    t = rf[1] + helper(src, rf[0], k - 1)
                    m = min(m, t)

            memo[(dst, k)] = m
            return m

        r = helper(src, dst, k + 1)
        if r == float("inf"):
            return -1
        return r
