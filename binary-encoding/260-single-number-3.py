class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for n in nums:
            diff ^= n

        key = (diff & diff-1) ^ diff

        r1 = 0
        r2 = 0
        for n in nums:
            if key & n != 0:
                r1 ^= n
            else:
                r2 ^= n

        return [r1, r2]