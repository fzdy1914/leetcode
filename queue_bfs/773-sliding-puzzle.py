from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = (1, 2, 3, 4, 5, 0)
        start = board[0] + board[1]
        start = tuple(start)

        def candidates(now):
            pos = list(now).index(0)
            rs = []

            if pos < 3:
                c = list(now)
                c[pos], c[pos + 3] = c[pos + 3], c[pos]
                rs.append(tuple(c))
            if pos >= 3:
                c = list(now)
                c[pos], c[pos - 3] = c[pos - 3], c[pos]
                rs.append(tuple(c))
            if pos % 3 != 2:
                c = list(now)
                c[pos], c[pos + 1] = c[pos + 1], c[pos]
                rs.append(tuple(c))
            if pos % 3 != 0:
                c = list(now)
                c[pos], c[pos - 1] = c[pos - 1], c[pos]
                rs.append(tuple(c))

            return rs

        q = [(start, 0)]
        visited = {start}

        while len(q) > 0:
            pair = q.pop(0)
            if pair[0] == target:
                return pair[1]

            for c in candidates(pair[0]):
                if c in visited:
                    continue

                visited.add(c)
                q.append((c, pair[1] + 1))

        return -1