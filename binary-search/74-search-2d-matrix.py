from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if matrix[mid][0] == target:
                return True

            if matrix[mid][0] < target:
                start = mid
            else:
                end = mid

        next_to_search = start
        if matrix[end][0] <= target:
            next_to_search = end

        start = 0
        end = len(matrix[0]) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if matrix[next_to_search][mid] == target:
                return True

            if matrix[next_to_search][mid] < target:
                start = mid
            else:
                end = mid

        if matrix[next_to_search][start] == target:
            return True

        if matrix[next_to_search][end] == target:
            return True

        return False