import queue
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # dp = [0] * (n)

        # q = queue.PriorityQueue()
        # dp[0] = nums[0]

        # q.put((-dp[0], 0))

        # for i in range(1, n):
        #     while q.queue[0][1] < max(0, i - k):
        #         q.get()

        #     dp[i] = -q.queue[0][0] + nums[i]

        #     if dp[i] > -q.queue[0][0]:
        #         q = queue.PriorityQueue()
        #     q.put((-dp[i], i))
        # return dp[-1]

        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        # mono-queue
        q = [dp[0]]

        for i in range(1, n):
            dp[i] = q[0] + nums[i]

            while len(q) > 0 and q[-1] < dp[i]:
                q.pop()
            q.append(dp[i])

            if i - k >= 0:
                if dp[i - k] == q[0]:
                    q.pop(0)

        return dp[-1]