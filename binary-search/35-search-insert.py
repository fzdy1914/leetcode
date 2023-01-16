from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        if target > nums[end]:
            return end + 1
        if target > nums[start]:
            return end

        return start