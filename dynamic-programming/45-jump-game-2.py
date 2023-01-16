from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        dp[0] = 0

        for i in range(len(nums)):
            if dp[i] != -1:
                for j in range(1, nums[i] + 1):
                    if i + j < len(nums):
                        if dp[i] + 1 < dp[i + j] or dp[i + j] < 0:
                            dp[i + j] = dp[i] + 1

        return dp[len(nums) - 1]
