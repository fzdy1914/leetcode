from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = {i: 0 for i in set(nums)}
        can = freq.copy()
        for n in nums:
            freq[n] += 1

        for idx in range(len(nums)):
            n = nums[idx]
            if freq[n] == 0:
                continue

            if can[n] > 0:
                can[n] -= 1
                if n + 1 in can:
                    can[n + 1] += 1
                freq[n] -= 1

                idx += 1
                continue

            if n + 1 in freq and n + 2 in freq and freq[n + 1] > 0 and freq[n + 2] > 0:
                freq[n] -= 1
                freq[n + 1] -= 1
                freq[n + 2] -= 1
                if n + 3 in can:
                    can[n + 3] += 1
                idx += 1
                continue
            else:
                return False

        return True