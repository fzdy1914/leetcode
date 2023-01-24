class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = 0
        for ss in s:
            r ^= ord(ss)

        for tt in t:
            r ^= ord(tt)

        return chr(r)