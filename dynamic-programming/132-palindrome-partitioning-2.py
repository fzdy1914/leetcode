class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(ss):
            return ss == ss[::-1]

        dp = {0: 0}

        for i in range(1, len(s) + 1):
            mini = 3000
            for j in range(0, i):
                if isPalindrome(s[j:i]):
                    if j == 0:
                        mini = 0
                    else:
                        new = dp[j] + 1
                        if new < mini:
                            mini = new
            dp[i] = mini

        return dp[len(s)]