from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        # max queue
        q = []
        for i in range(1, n):
            v = dp[i - 1]
            while len(q) > 0 and q[-1] < v:
                q.pop()
            q.append(v)

            dp[i] = max(q[0] + nums[i], nums[i])

            if i >= k:
                if dp[i - k] == q[0]:
                    q.pop(0)

        return max(dp)
