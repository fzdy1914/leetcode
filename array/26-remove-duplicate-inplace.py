from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow = 0
        fast = 1

        while fast < n:
            if nums[fast] == nums[slow]:
                fast += 1
                continue

            slow = slow + 1
            nums[slow], nums[fast] = nums[fast], nums[slow]

            fast = fast + 1

        return slow + 1