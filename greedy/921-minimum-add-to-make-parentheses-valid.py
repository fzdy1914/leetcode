class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        not_matched = 0
        left = 0

        for ss in s:
            if ss == "(":
                if left < 0:
                    not_matched -= left
                    left = 0
                left += 1
            else:
                left -= 1

        if left < 0:
            not_matched -= left
        else:
            not_matched += left
        return not_matched