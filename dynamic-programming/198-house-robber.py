from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        stole, not_stole = 0, 0

        for n in nums:
            new_stole = not_stole + n
            new_not_stole = max(not_stole, stole)

            stole = new_stole
            not_stole = new_not_stole

        return max(stole, not_stole)