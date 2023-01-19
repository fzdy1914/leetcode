class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = (nums[i] + prefix_sum[i]) % k

        print(prefix_sum)
        cnt = 0

        rs = [0] * k
        for i in range(n):
            cnt += rs[prefix_sum[i + 1]]
            rs[prefix_sum[i + 1]] += 1

            if prefix_sum[i + 1] == 0:
                cnt += 1

        return cnt
