from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = list()
        seen = set()

        n = len(mat)
        m = len(mat[0])

        for mm in mat:
            nn = mm.copy()
            for i in range(m):
                nn[i] = float("inf")
            result.append(nn)

        queue = list()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))

        while len(queue) > 0:
            pos = queue.pop(0)

            if pos[2] < result[pos[0]][pos[1]]:
                result[pos[0]][pos[1]] = pos[2]

                if pos[0] > 0:
                    queue.append((pos[0] - 1, pos[1], pos[2] + 1))
                if pos[0] < n - 1:
                    queue.append((pos[0] + 1, pos[1], pos[2] + 1))
                if pos[1] > 0:
                    queue.append((pos[0], pos[1] - 1, pos[2] + 1))
                if pos[1] < m - 1:
                    queue.append((pos[0], pos[1] + 1, pos[2] + 1))

        return result