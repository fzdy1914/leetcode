class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = []
        def backtrack(ss, path):
            for word in wordDict:
                if ss.startswith(word):
                    new_path = list(tuple(path))
                    new_path.append(word)
                    if ss == word:
                        result.append(new_path)
                    else:
                        backtrack(ss[len(word):], new_path)

        backtrack(s, [])

        final_res = []
        for r in result:
            final_res.append(" ".join(r))
        return final_res
