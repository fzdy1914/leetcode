class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        r = []

        def backtrack(ss, path):
            if len(path) == 4:
                if ss == "":
                    r.append(".".join(path))
                return

            m = min(3, len(ss))
            for i in range(1, m+1):
                if int(ss[:i]) <= 255 and str(int(ss[:i])) == ss[:i]:
                    new_path = path.copy()
                    new_path.append(ss[:i])

                    backtrack(ss[i:], new_path)

        backtrack(s, [])

        return r