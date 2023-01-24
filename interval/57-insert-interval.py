from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = intervals.copy()
        idx = 0
        for interval in intervals:
            if interval[1] < newInterval[0]:
                idx += 1
                continue
            if interval[0] > newInterval[1]:
                break
            newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            result.remove(interval)

        result.insert(idx, newInterval)
        return result