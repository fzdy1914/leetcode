import math


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count(n):
            if n == 0:
                return 0

            cnt = 0
            # TODO: math.log
            k = int(math.log(n) / math.log(5))

            for i in range(k):
                cnt += n // (5 ** (i + 1))

            return cnt

        start = 0
        end = 10 ** 10
        while start + 1 < end:
            mid = start + (end - start) // 2
            if count(mid) >= k:
                end = mid
            else:
                start = mid

        if count(start) == k:
            left = start
        else:
            left = end

        start = 0
        end = 10 ** 10
        while start + 1 < end:
            mid = start + (end - start) // 2
            if count(mid) >= k + 1:
                end = mid
            else:
                start = mid

        if count(start) == k + 1:
            right = start
        else:
            right = end

        return right - left