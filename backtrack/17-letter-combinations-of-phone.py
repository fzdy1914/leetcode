from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        r = []

        def backtrack(d, path):
            if len(d) == 0:
                if path != "":
                    r.append(path)
                return

            candidate = dic[d[0]]
            for c in candidate:
                backtrack(d[1:], path + c)

        backtrack(digits, "")
        return r