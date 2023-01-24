from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        idx = 0
        nums.insert(0, 0)

        while idx < len(nums):
            if nums[idx] == idx:
                idx += 1
                continue

            prev = idx
            temp = nums[idx]

            while temp != prev and temp != nums[temp]:
                t = nums[temp]
                nums[temp] = temp
                temp = t

            nums[prev] = temp
            idx += 1

        for i in range(len(nums)):
            if i != nums[i]:
                return [nums[i], i]