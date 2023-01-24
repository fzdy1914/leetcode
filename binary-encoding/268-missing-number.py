from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = len(nums)
        for i, n in enumerate(nums):
            r ^= i
            r ^= n

        return r