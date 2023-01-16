class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rs = []

        for i in range(m):
            r = []
            for j in range(n):
                if i == 0 and j == 0:
                    r.append(1)
                elif i == 0:
                    r.append(1)
                elif j == 0:
                    r.append(1)
                else:
                    k = rs[i - 1][j] + r[j - 1]
                    r.append(k)

            rs.append(r)
        return rs[-1][-1]