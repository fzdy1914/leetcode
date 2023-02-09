from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = dict()
        for i in ideas:
            if i[0] in d:
                d[i[0]].add(i[1:])
            else:
                d[i[0]] = {i[1:]}

        l = list(d.items())

        n = 0

        for i in range(1, len(l)):
            for j in range(i):
                left = l[i][1]
                right = l[j][1]

                ll = left - right
                rr = right - left
                n += 2 * len(ll) * len(rr)

        return n