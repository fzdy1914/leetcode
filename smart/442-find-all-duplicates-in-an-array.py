from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.insert(0, 0)
        rs = []

        for i in range(1, len(nums)):
            v = nums[i] if nums[i] > 0 else -nums[i]
            if nums[v] > 0:
                nums[v] *= -1
            else:
                rs.append(v)

        return rs