from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt = 0
        for n in nums:
            if n == 0:
                cnt += 1

        if cnt <= k:
            return len(nums)

        left = 0
        right = 0
        remain = k
        r = 0
        while right < len(nums):
            c = nums[right]
            right += 1

            if c == 0:
                remain -= 1

            while left < right:
                if remain > 0:
                    break
                if remain == 0:
                    r = max(right - left, r)
                    break
                cc = nums[left]
                if cc == 0:
                    remain += 1
                left += 1

        return r