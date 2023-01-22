from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        total = list(range(1, n + 1))

        result = []
        def backtrack(remains, path):
            if len(path) == k:
                result.append(path.copy())
                return

            for i in range(len(remains)):
                path.append(remains[i])

                backtrack(remains[i+1:], path)

                path.pop()

        backtrack(total, [])

        return result