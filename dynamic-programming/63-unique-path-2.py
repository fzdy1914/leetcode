class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            dp.append([0] * n)

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    dp[0][0] = 1
                elif i == 0:
                    dp[0][j] = dp[0][j-1]
                elif j == 0:
                    dp[i][0] = dp[i-1][0]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]