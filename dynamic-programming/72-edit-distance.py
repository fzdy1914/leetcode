class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = []
        for i in range(m + 1):
            dp.append([0] * (n + 1))

        for i in range(m + 1):
            for j in range(n + 1):
                if i==0 and j==0:
                    dp[0][0] = 0
                elif i==0:
                    dp[i][j] = j
                elif j==0:
                    dp[i][j] = i
                else:
                    if text1[i-1] != text2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i-1][j-1]
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]