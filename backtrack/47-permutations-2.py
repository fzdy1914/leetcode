from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def backtrack(remain, path):
            s = set()
            for r in remain:
                if r in s:
                    continue
                else:
                    s.add(r)
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