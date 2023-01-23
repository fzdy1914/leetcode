from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1


        start = 1
        end = len(nums) - 2

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                start = mid
            elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
                end = mid
            else:
                end = mid


        if nums[start - 1] < nums[start] and nums[start] > nums[start + 1]:
                return start

        return end