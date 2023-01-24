from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(a, k):
            for i in range((k + 1) // 2):
                a[i], a[k - i] = a[k - i], a[i]

        path = []
        for i in reversed(range(1, len(arr) + 1)):
            idx = arr.index(i)
            if idx == i - 1:
                continue

            if idx == 0:
                path.append(i)
                flip(arr, i - 1)
                continue

            path.append(idx + 1)
            path.append(i)
            flip(arr, idx)
            flip(arr, i - 1)

        return path