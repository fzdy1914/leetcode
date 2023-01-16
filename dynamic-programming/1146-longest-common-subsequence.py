class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = []
        for i in range(m):
            dp.append([0] * n)

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    if text1[0] == text2[0]:
                        dp[0][0] = 1
                elif i==0:
                    if text1[i] == text2[j]:
                        dp[0][j] = 1
                    else:
                        dp[0][j] = dp[0][j-1]
                elif j==0:
                    if text1[i] == text2[j]:
                        dp[i][0] = 1
                    else:
                        dp[i][0] = dp[i-1][0]
                else:
                    if text1[i] == text2[j]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]