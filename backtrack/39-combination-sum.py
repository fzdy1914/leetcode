from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(t, cs, path):
            for i in range(len(cs)):
                if cs[i] > t:
                    continue

                new_path = path.copy()
                new_path.append(cs[i])
                if cs[i] == t:
                    result.append(new_path)
                else:
                    backtrack(t - cs[i], cs[i:], new_path)

        backtrack(target, candidates, [])

        return result