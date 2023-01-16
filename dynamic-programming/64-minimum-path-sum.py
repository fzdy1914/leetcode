from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rs = []
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            r = []
            for j in range(m):
                if i == 0 and j == 0:
                    r.append(grid[0][0])
                elif i == 0:
                    r.append(grid[0][j] + r[j - 1])
                elif j == 0:
                    r.append(rs[i - 1][0] + grid[i][0])
                else:
                    k = min(rs[i - 1][j], r[j - 1]) + grid[i][j]
                    r.append(k)

            rs.append(r)
        return rs[-1][-1]
