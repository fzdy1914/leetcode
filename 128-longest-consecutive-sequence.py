from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = [0] * len(nums)

        idx_mp = dict()

        for i in range(len(nums)):
            idx_mp[nums[i]] = i

        m = 0
        idx = 0
        while idx < len(nums):
            if visited[idx] == 1:
                idx += 1
                continue

            visited[idx] = 1

            low = nums[idx] - 1
            while low in idx_mp:
                visited[idx_mp[low]] = 1
                low = low - 1

            high = nums[idx] + 1
            while high in idx_mp:
                visited[idx_mp[high]] = 1
                high = high + 1

            new = high - low - 1
            if new > m:
                m = new
        return m