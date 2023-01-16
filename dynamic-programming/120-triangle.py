from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        new = []

        for i in range(len(triangle)):
            if i == 0:
                new.append(triangle[i])
                continue

            result = []
            for j in range(i + 1):
                if j == 0:
                    result.append(triangle[i][j] + new[i-1][j])
                elif j == i :
                    result.append(triangle[i][j] + new[i-1][j-1])      
                else: 
                    result.append(min(triangle[i][j] + new[i-1][j-1], triangle[i][j] + new[i-1][j]))

            new.append(result)

        return min(new[-1])      