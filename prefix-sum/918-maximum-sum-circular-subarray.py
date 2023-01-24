from typing import List


class Solution:
    # TODO: try prefix-sum when encountering subarray sum !!!
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        p_sum = [0] * (n + 1)

        r = float("-inf")
        for i in range(n):
            p_sum[i + 1] = p_sum[i] + nums[i]
        t_sum = p_sum[-1]

        min_q = float("inf")
        max_q = float("-inf")
        for i in range(1, n + 1):
            v = p_sum[i - 1]
            min_q = min(min_q, v)
            max_q = max(max_q, v)

            s = p_sum[i] - min_q
            r = max(r, s)

            s = p_sum[i] - max_q
            if t_sum-s != 0:
                r = max(r, t_sum-s)

        return r