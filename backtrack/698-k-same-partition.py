from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        total = sum(nums)
        even = int(total / k)
        if even * k != total:
            return False

        candidate = []

        nums.sort()

        def backtrack(remains, path):
            if sum(path) == even:
                candidate.append(path.copy())
                return

            for i in range(len(remains)):
                if i > 0 and remains[i] == remains[i - 1]:
                    continue

                path.append(remains[i])

                backtrack(remains[i + 1:], path)

                path.pop()

        backtrack(nums, [])

        for c in candidate:
            nums_c = nums.copy()
            for cc in c:
                nums_c.remove(cc)

            if self.canPartitionKSubsets(nums_c, k - 1):
                return True

        return False