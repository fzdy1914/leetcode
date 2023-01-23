from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))

        result = []

        def backtrack(remains, path):
            if len(path) > k:
                return

            if len(path) == k:
                if sum(path) == n:
                    result.append(path.copy())

                return

            for i in range(len(remains)):
                path.append(remains[i])
                backtrack(remains[i + 1:], path)
                path.pop()

        backtrack(candidates, [])
        return result