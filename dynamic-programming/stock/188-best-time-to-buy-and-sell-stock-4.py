from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        status = [0] + [float("-inf")] * (2 * k)

        for price in prices:
            prev = status.copy()
            for i in range(1, 2 * k + 1):
                status[i] = max(prev[i], prev[i - 1] + (-1) ** (i % 2) * price)

        result = [status[i] for i in range(len(status)) if i % 2 == 0]
        return max(result)