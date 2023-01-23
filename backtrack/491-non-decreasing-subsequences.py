from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def backtrack(remains, path):
            if len(path) >= 2:
                result.add(tuple(path))

            for i in range(len(remains)):
                if len(path) == 0 or path[-1] <= remains[i]:
                    path.append(remains[i])

                    backtrack(remains[i+1:], path)

                    path.pop()

        backtrack(nums, [])

        return list(result)