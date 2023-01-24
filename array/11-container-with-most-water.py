from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        r = 0
        while left < right:
            cur = (right - left) * min(height[left], height[right])

            r = max(r, cur)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return r