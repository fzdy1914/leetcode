from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            # while start < end and nums[start] == nums[start + 1] :
            #     start += 1
            # while start < end and nums[end] == nums[end - 1]:
            #     end -= 1

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True

            if nums[start] < nums[mid]:
                if nums[mid] >= target >= nums[start]:
                    end = mid
                else:
                    start = mid
            elif nums[start] > nums[mid]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[end - 1] == nums[end]:
                    end -= 1
                elif nums[start + 1] == nums[start]:
                    start += 1

        if nums[start] == target:
            return True

        if nums[end] == target:
            return True

        return False
