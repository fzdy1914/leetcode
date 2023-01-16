class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r_set = set()

        left = 0
        right = 0 
        result = 0
        while right < len(s):
            c = s[right]
            right += 1

            if c not in r_set:
               r_set.add(c)
               result = max(result, right - left)
               continue

            while left < right:
                cc = s[left]
                left += 1
                if cc == c:
                    result = max(result, right - left)
                    break
                else:
                    r_set.remove(cc)

        return result