from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))

        cur_max = -1
        prev_start = -1

        rs = []

        for i in intervals:
            if i[0] > cur_max:
                if cur_max != -1:
                    rs.append([prev_start, cur_max])

                cur_max = i[1]
                prev_start = i[0]

            else:
                cur_max = max(cur_max, i[1])

        if cur_max != -1:
            rs.append([prev_start, cur_max])

        return rs