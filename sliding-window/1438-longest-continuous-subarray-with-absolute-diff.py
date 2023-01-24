import bisect
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # TODO: can optimize using max/min deque
        temp = []

        left = 0
        right = 0
        r = 0

        while right < len(nums):
            c = nums[right]
            right += 1

            bisect.insort(temp, c)

            while left < right:
                if (temp[-1] - temp[0]) <= limit:
                    r = max(r, right - left)
                    break

                cc = nums[left]
                left += 1
                temp.remove(cc)

        return r