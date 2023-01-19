from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        zero_index = 0
        product = 1

        l = len(nums)
        result = [0] * l

        for i in range(l):
            if nums[i] == 0:
                zero_count += 1
                if zero_count > 1:
                    return [0] * l
                zero_index = i
            else:
                product *= nums[i]

        if zero_count == 1:
            result[zero_index] = product
        else:
            for i in range(l):
                result[i] = int(product / nums[i])

        return result