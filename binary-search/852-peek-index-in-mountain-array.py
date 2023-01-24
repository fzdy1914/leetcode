from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 1
        end = len(arr) - 2

        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid + 1] > arr[mid] > arr[mid - 1]:
                start = mid
            else:
                end = mid

        if arr[start] > arr[start - 1] and arr[start] > arr[start + 1]:
            return start

        return end