from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]

        rs = 0
        for i in range(1, len(prices)):
            r = prices[i] - cur_min
            rs = max(rs, r)

            cur_min = min(cur_min, prices[i])

        return rs
