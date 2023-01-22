import queue
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n)

        q = queue.PriorityQueue()
        dp[0] = nums[0]

        # TODO max heap
        q.put((-dp[0], 0))

        for i in range(1, n):
            # TODO heap peek
            while q.queue[0][1] < max(0, i - k):
                q.get()

            dp[i] = -q.queue[0][0] + nums[i]

            if dp[i] > -q.queue[0][0]:
                q = queue.PriorityQueue()
            q.put((-dp[i], i))
        return dp[-1]