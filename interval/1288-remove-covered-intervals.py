from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))

        rs = 0

        current_max = 0
        for i in intervals:
            if i[1] <= current_max:
                continue
            rs += 1
            current_max = i[1]

        return rs