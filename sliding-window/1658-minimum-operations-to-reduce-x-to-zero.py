from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = sum(nums)
        target = s - x
        if target == 0:
            return n

        l = -1

        left = 0
        right = 0

        while right < n:
            c = nums[right]
            right += 1
            target -= c

            while left < right:
                if target == 0:
                    l = max(l, right - left)
                    break

                if target > 0:
                    break

                cc = nums[left]
                left += 1
                target += cc

        if l == -1:
            return l
        return n - l
