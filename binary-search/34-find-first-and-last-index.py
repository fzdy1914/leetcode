import math
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # leftIdx = bisect.bisect_left(nums, target)
        # if leftIdx > len(nums) - 1 or nums[leftIdx] != target:
        #     return [-1, -1]

        # rightIdx = bisect.bisect_right(nums, target)

        # return [leftIdx, rightIdx - 1]

        if len(nums) == 0:
            return [-1, -1]

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            leftIdx = start
        elif nums[end] == target:
            leftIdx = end
        else:
            return [-1, -1]

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            rightIdx = end
        elif nums[start] == target:
            rightIdx = start

        return [leftIdx, rightIdx]