from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(remains, path, target):
            for i in range(len(remains)):
                if i > 0 and remains[i] == remains[i - 1]:
                    continue

                path.append(remains[i])
                if remains[i] == target:
                    result.append(path.copy())
                    path.pop()
                    return

                if remains[i] < target:
                    backtrack(remains[i+1:], path, target - remains[i])

                path.pop()

        backtrack(candidates, [], target)

        return result