import bisect
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = {c:[] for c in set(s)}
        for idx, c in enumerate(s):
            d[c].append(idx)

        ok = 0
        for word in words:
            can = True
            idx = 0
            idx_s = 0
            while idx < len(word):
                c = word[idx]

                if c not in d:
                    can = False
                    break

                new_i = bisect.bisect_left(d[c], idx_s)
                if new_i == len(d[c]):
                    can = False
                    break

                idx_s = d[c][new_i] + 1
                idx += 1

            if can:
                ok += 1
        return ok