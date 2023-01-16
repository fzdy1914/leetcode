class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r_dict = dict()
        for s in s1:
            if s in r_dict:
                r_dict[s] += 1
            else:
                r_dict[s] = 1

        def finished():
            for k, v in r_dict.items():
                if v != 0:
                    return False

            return True

        left = 0
        right = 0

        while right < len(s2):
            right += 1
            c = s2[right - 1]
            if c in r_dict:
                r_dict[c] -= 1

            if right - left < len(s1):
                continue

            while left < right:
                c = s2[left]

                # TODO: can shrink together with can track
                if right - left == len(s1):
                    if finished():
                        return True
                    break
                else:
                    left += 1
                    if c in r_dict:
                        r_dict[c] += 1

        return False