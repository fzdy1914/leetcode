from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            mini = -1

            for c in coins:
                if i - c < 0:
                    continue
                if dp[i - c] == -1:
                    continue
                if mini == -1:
                    mini = dp[i - c] + 1
                else:
                    mini = min(dp[i - c] + 1, mini)

            dp[i] = mini
        return dp[-1]