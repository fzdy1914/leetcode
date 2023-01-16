from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def find(i):
            while i < n:
                j = 0
                while j < m:
                    if grid[i][j] == "1":
                        return (i, j)
                    j += 1
                i += 1
            return None

        def polute(pos):
            if grid[pos[0]][pos[1]] == "0":
                return

            grid[pos[0]][pos[1]] = "0"

            if pos[0] > 0:
                polute((pos[0] - 1, pos[1]))
            if pos[0] < n - 1:
                polute((pos[0] + 1, pos[1]))
            if pos[1] > 0:
                polute((pos[0], pos[1] - 1))
            if pos[1] < m - 1:
                polute((pos[0], pos[1] + 1))

        count = 0
        a = 0
        while True:
            p = find(a)
            if p is None:
                return count

            a = p[0]
            count += 1
            polute(p)