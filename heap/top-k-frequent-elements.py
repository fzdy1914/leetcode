import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {n:0 for n in set(nums)}

        for n in nums:
            d[n] += 1

        q = [(-v, k) for k, v in d.items()]

        heapq.heapify(q)

        r = []
        while k > 0:
            item = heapq.heappop(q)
            r.append(item[1])
            k-=1

        return r