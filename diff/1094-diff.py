from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001

        for t in trips:
            diff[t[1]] += t[0]
            diff[t[2]] -= t[0]

        r = diff[0]
        if r > capacity:
            return False
        for i in range(1, 1001):
            r += diff[i]
            if r > capacity:
                return False

        return True
