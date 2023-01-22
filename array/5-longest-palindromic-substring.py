class Solution:
    def longestPalindrome(self, s: str) -> str:
        dummy = ""
        result = ""

        for i in range(len(s)):
            dummy += s[i]
            if i != len(s) - 1:
                dummy += "_"

        for i in range(0, len(dummy)):
            left = i
            right = i

            while left > 0 and right < len(dummy) - 1 and dummy[left-1] == dummy[right+1]:
                left -= 1
                right += 1

            r = dummy[left:right +1].replace("_", "")
            if len(r) > len(result):
                result = r

        return result
