from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calc(lst):
            result = []
            weight = 0
            for i in reversed(lst):
                weight += i[1]
                result.append(weight * i[0])
            return max(result)

        m = 0
        stack = []
        for h in heights:
            if len(stack) == 0 or stack[-1][0] < h:
                stack.append((h, 1))
            elif stack[-1][0] == h:
                stack[-1] = (h, stack[-1][1] + 1)
            else:
                # TODO: pop optimization
                result = calc(stack)
                if result > m:
                    m = result
                new_len = 1
                while len(stack) > 0 and stack[-1][0] > h:
                    p = stack.pop()
                    new_len += p[1]
                stack.append((h, new_len))

        result = calc(stack)
        if result > m:
            m = result

        return m
