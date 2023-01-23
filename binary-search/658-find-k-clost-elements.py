import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        idx = bisect.bisect_left(arr, x)

        if idx == 0:
            return arr[:k]
        elif idx == n:
            return arr[-k:]

        if arr[idx] - x >= x - arr[idx - 1]:
            idx -= 1

        left = idx
        right = idx
        remain = k - 1
        rs = [arr[idx]]

        while remain > 0:
            if left == 0:
                right += 1
                rs.append(arr[right])
                remain -= 1
            elif right == n - 1:
                left -= 1
                rs.insert(0, arr[left])
                remain -= 1
            else:
                if arr[right + 1] - x >= x - arr[left - 1]:
                    left -= 1
                    rs.insert(0, arr[left])
                    remain -= 1
                else:
                    right += 1
                    rs.append(arr[right])
                    remain -= 1
        return rs