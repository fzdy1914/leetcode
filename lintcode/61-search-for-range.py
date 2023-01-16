from typing import (
    List,
)


class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def search_range(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        # write your code here
        start = 0
        end = len(nums) - 1

        left = -1
        right = -1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            right = start

        if nums[end] == target:
            right = end

        if right == -1:
            return [-1, -1]

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            left = end

        if nums[start] == target:
            left = start

        return [left, right]