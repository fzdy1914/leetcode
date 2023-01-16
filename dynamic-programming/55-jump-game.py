from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # TODO more carefully of recursive status
        n, next_max = len(nums), 0
        for x in range(n):
            if x > next_max:
                return False
            next_max = max(next_max, nums[x] + x)
        if next_max >= n-1:
            return True
        return False
