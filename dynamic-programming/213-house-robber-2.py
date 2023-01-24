from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # stole first
        stole, not_stole = nums[0], 0

        for n in nums[1:]:
            new_stole = not_stole + n
            new_not_stole = max(not_stole, stole)

            stole = new_stole
            not_stole = new_not_stole

        r = not_stole

        # not stole first
        stole, not_stole = 0, 0

        for n in nums[1:]:
            new_stole = not_stole + n
            new_not_stole = max(not_stole, stole)

            stole = new_stole
            not_stole = new_not_stole

        return max(stole, not_stole, r)
