from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                end -= 1
        return min(nums[start], nums[end])