from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0

        cnt = 0
        while True:
            if fast == len(nums):
                break

            if nums[fast] == val:
                cnt += 1
                fast += 1
                continue

            nums[slow] = nums[fast]
            slow += 1
            fast += 1

        return len(nums) - cnt
