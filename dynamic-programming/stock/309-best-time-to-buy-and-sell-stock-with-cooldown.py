from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold, cur_not_hold_freeze = -float('inf'), 0, 0

        for stock_price in prices:
            prev_hold, prev_not_hold, prev_not_hold_freeze = cur_hold, cur_not_hold, cur_not_hold_freeze

            cur_hold = max(prev_hold, prev_not_hold - stock_price)

            cur_not_hold = max(prev_not_hold, prev_not_hold_freeze)

            cur_not_hold_freeze = prev_hold + stock_price

        return max(cur_not_hold, cur_not_hold_freeze)
