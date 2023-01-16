from typing import (
    List,
)


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        # write your code here
        if m >= sum(a):
            return sum(v)

        dp = []
        for i in range(len(a)):
            dp.append([0] * (m + 1))

        for i in range(len(a)):
            for j in range(m + 1):
                if i == 0:
                    dp[i][j] = v[i] if a[i] <= j else 0
                else:
                    if j - a[i] < 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        new = dp[i-1][j- a[i]] + v[i]
                        dp[i][j] = max(dp[i-1][j], new)
        return dp[-1][-1]
