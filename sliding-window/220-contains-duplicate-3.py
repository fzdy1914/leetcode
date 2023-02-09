import bisect
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        left = 0
        right = 0
        lst = []

        while right < len(nums):
            c = nums[right]
            right += 1

            if len(lst) == 0:
                lst.append(c)
            else:
                idx = bisect.bisect_left(lst, c)
                if idx == len(lst):
                    if abs(c - lst[-1]) <= valueDiff:
                        return True
                elif idx == 0:
                    if abs(c - lst[0]) <= valueDiff:
                        return True
                else:
                    if abs(c - lst[idx]) <= valueDiff or abs(c - lst[idx - 1]) <= valueDiff:
                        return True

                bisect.insort(lst, c)

            if len(lst) > indexDiff:
                cc = nums[left]
                left += 1
                lst.remove(cc)

        return False