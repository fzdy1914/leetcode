from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(remain, path):
            result.append(path)

            s = set()
            for i in range(len(remain)):
                if remain[i] in s:
                    continue
                else:
                    s.add(remain[i])

                new_path = path.copy()
                new_path.append(remain[i])
                backtrack(remain[i+1:], new_path)

        backtrack(nums, [])
        return list(result)
