import bisect
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p_sum = [0] * (n + 1)

        r = 100000

        for i in range(n):
            p_sum[i + 1] = p_sum[i] + nums[i]

        q = []
        for i in range(n):
            while len(q) > 0 and q[-1] > (p_sum[i], i):
                q.pop()
            q.append((p_sum[i], i))

            idx = bisect.bisect_left(q, (p_sum[i + 1] - k, 1000000))
            if idx == 0:
                continue
            r = min(r, i + 1 - q[idx - 1][1])

        if r == 100000:
            return -1

        return r