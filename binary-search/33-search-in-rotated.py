from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[start] < nums[mid]:
                if nums[mid] > target >= nums[start]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1
