class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(ss):
            for i in range(len(ss) // 2):
                if ss[i] != ss[len(ss) - 1 - i]:
                    return False
            return True

        r = []

        def backtrack(remain, path):
            if len(remain) == 0:
                r.append(path)
                return

            for i in range(1, len(remain) + 1):
                if isPalindrome(remain[:i]):
                    p = path.copy()
                    p.append(remain[:i])
                    backtrack(remain[i:], p)

        backtrack(s, [])

        return r