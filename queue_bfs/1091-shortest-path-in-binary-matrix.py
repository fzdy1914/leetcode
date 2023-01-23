from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        m = len(grid)
        n = len(grid[0])

        visited = {(0, 0)}
        q = [((0, 0), 1)]

        while len(q) > 0:
            node = q.pop(0)
            pos = node[0]
            step = node[1]

            if pos[0] == m - 1 and pos[1] == n - 1:
                return step

            possibles = []
            if pos[0] > 0:
                possibles.append((pos[0] - 1, pos[1]))
                if pos[1] > 0:
                    possibles.append((pos[0] - 1, pos[1] - 1))
                if pos[1] < n - 1:
                    possibles.append((pos[0] - 1, pos[1] + 1))

            if pos[0] < m - 1:
                possibles.append((pos[0] + 1, pos[1]))
                if pos[1] > 0:
                    possibles.append((pos[0] + 1, pos[1] - 1))
                if pos[1] < n - 1:
                    possibles.append((pos[0] + 1, pos[1] + 1))
            if pos[1] > 0:
                possibles.append((pos[0], pos[1] - 1))
            if pos[1] < n - 1:
                possibles.append((pos[0], pos[1] + 1))

            for p in possibles:
                if p in visited or grid[p[0]][p[1]] == 1:
                    continue
                visited.add(p)
                q.append((p, step + 1))

        return -1