from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = dict()
        dp[nums[0]] = [nums[0]]
        global_max = [nums[0]]

        for i in range(1, len(nums)):
            maxi = []
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if len(dp[nums[j]]) > len(maxi):
                        maxi = dp[nums[j]].copy()
            maxi.append(nums[i])
            dp[nums[i]] = maxi
            if len(maxi) > len(global_max):
                global_max = maxi

        return global_max