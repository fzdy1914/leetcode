from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def allValid(path):
            m = len(path)
            if m == 0:
                return list(range(n))
            result = []
            for i in range(n):
                isValid = True
                for j in range(m):
                    if path[j][i] == "Q":
                        isValid = False
                        break

                    if j >= m - i and path[j][i - m + j] == "Q":
                        isValid = False
                        break

                    if j >= m - n + 1 + i and path[j][m - j + i] == "Q":
                        isValid = False
                        break
                if isValid:
                    result.append(i) 
            return result

        def backtrack(path):
            if len(path) == n:
                result.append(path.copy())
                return

            for p in allValid(path):
                s = ["."] * n
                s[p] = "Q"
                path.append("".join(s))
                backtrack(path)
                path.pop()

        backtrack([])
        return result