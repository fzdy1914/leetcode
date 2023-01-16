from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums) + 1)
        n = len(nums)
        for i in range(1, n):
            m = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    m = max(m, dp[j] + 1)
            dp[i] = m

        return max(dp)
