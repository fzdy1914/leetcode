from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_unhold = 0
        current_hold_once = float("-inf")
        current_unhold_once = float("-inf")
        current_hold_twice = float("-inf")
        current_unhold_twice = float("-inf")

        for price in prices:
            prev_1 = current_unhold
            prev_2 = current_hold_once
            prev_3 = current_unhold_once
            prev_4 = current_hold_twice
            prev_5 = current_unhold_twice

            current_unhold = prev_1
            current_hold_once = max(prev_2, prev_1 - price)
            current_unhold_once = max(prev_3, prev_2 + price)
            current_hold_twice = max(prev_4, prev_3 - price)
            current_unhold_twice = max(prev_5, prev_4 + price)

        return max(current_unhold, current_unhold_once, current_unhold_twice)