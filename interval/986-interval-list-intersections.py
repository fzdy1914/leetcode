from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        rs = []

        i_1 = 0
        i_2 = 0

        while i_1 < len(firstList) and i_2 < len(secondList):
            maxi = max(firstList[i_1][0], secondList[i_2][0])
            a = True
            if firstList[i_1][1] < secondList[i_2][1]:
                mini = firstList[i_1][1]
            else:
                mini = secondList[i_2][1]
                a = False

            if a:
                i_1 += 1
            else:
                i_2 += 1

            if maxi <= mini:
                rs.append([maxi, mini])

        return rs