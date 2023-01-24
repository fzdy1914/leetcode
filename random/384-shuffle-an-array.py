import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.old = nums.copy()
        self.new = nums

    def reset(self) -> List[int]:
        self.new = self.old.copy()
        return self.old

    def shuffle(self) -> List[int]:
        for i in range(len(self.new)):
            r = random.randrange(len(self.new))

            self.new[i], self.new[r] = self.new[r], self.new[i]
        return self.new