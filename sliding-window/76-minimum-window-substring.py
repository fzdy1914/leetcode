# TODO: Do for a simple version first
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        r_dict = dict()
        for tt in t:
            if tt in r_dict:
                r_dict[tt] += 1
            else:
                r_dict[tt] = 1

        def finished():
            for k, v in r_dict.items():
                if v > 0:
                    return False

            return True

        left = 0
        right = 0
        mini = float("inf")
        result = ""
        while right < len(s):
            right += 1
            c = s[right - 1: right]
            if c not in r_dict:
                continue

            r_dict[c] -= 1

            while left < right:
                cc = s[left: left+1]
                if cc not in r_dict:
                    left += 1
                    continue

                # TODO: check first, then, see if can shrink
                if r_dict[cc] > 0:
                    break
                elif r_dict[cc] == 0:
                    if finished():
                        if right - left < mini:
                            mini = right - left
                            result = s[left: right]
                    break
                else:
                    r_dict[cc] += 1
                    left += 1
        return result