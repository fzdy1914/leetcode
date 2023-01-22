from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [costs[0]]

        for i in range(1, len(costs)):
            a = min(dp[-1][1], dp[-1][2]) + costs[i][0]
            b = min(dp[-1][0], dp[-1][2]) + costs[i][1]
            c = min(dp[-1][0], dp[-1][1]) + costs[i][2]

            dp.append([a, b, c])

        return min(dp[-1])