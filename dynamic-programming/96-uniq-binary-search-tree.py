class Solution:
    def numTrees(self, n: int) -> int:
        dp = {-1: 1, 0: 1}

        for i in range(1, n):
            s = 0
            for j in range(0, i+1):
                left = dp[j - 1]
                right = dp[i - j - 1]
                s += left * right

            dp[i] = s

        return dp[n-1]
