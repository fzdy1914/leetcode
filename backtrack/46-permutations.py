from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(remain, path):
            for r in remain:
                new = remain.copy()
                new.remove(r)

                p_new = path.copy()
                p_new.append(r)

                if len(new) == 0:
                    result.append(p_new)
                else:
                    backtrack(new, p_new)

        backtrack(nums, [])
        return result