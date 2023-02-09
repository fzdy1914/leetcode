class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        count = {i: 0 for i in set(list(s))}
        for c in s:
            count[c] += 1

        min_k = None
        for i, v in count.items():
            if v < k:
                min_k = i
                break
        if min_k is None:
            return len(s)

        r = 0
        for ss in s.split(min_k):
            r = max(r, self.longestSubstring(ss, k))

        return r
