import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.d = {c: [] for c in set(nums)}
        for idx, n in enumerate(nums):
            self.d[n].append(idx)

    def pick(self, target: int) -> int:
        l = len(self.d[target])
        r = random.randrange(l)
        return self.d[target][r]
