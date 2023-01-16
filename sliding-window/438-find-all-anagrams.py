class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r_dict = dict()
        for pp in p:
            if pp in r_dict:
                r_dict[pp] += 1
            else:
                r_dict[pp] = 1

        def check():
            for k, v in r_dict.items():
                if v != 0:
                    return False
            return True

        result = []

        left = 0
        right = 0

        while right < len(s):
            c = s[right]
            right += 1

            if c in r_dict:
                r_dict[c] -= 1

            while left < right:
                if right - left < len(p):
                    break

                if right - left == len(p):
                    if check():
                        result.append(left)
                    break

                cc = s[left]
                left += 1
                if cc in r_dict:
                    r_dict[cc] += 1

        return result