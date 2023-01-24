from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TODO: max deque and how to use it!!!
        max_deque = []

        left = 0
        right = 0
        rs = []

        while right < len(nums):
            c = nums[right]
            right += 1

            while len(max_deque) > 0 and max_deque[-1] < c:
                max_deque.pop()
            max_deque.append(c)

            while left < right:
                if right - left < k:
                    break

                if right - left == k:
                    rs.append(max_deque[0])
                    break

                cc = nums[left]
                left += 1

                if cc == max_deque[0]:
                    max_deque.pop(0)

        return rs