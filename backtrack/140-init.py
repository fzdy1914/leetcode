class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def start_with(ss):
            cur_result = []
            for word in wordDict:
                if ss.startswith(word):
                    print(word)
                    if ss == word:
                        cur_result.append([word,])
                    else:
                        rest = ss[len(word):]
                        result = start_with(rest)

                        for r in result:
                            r.insert(0, word)
                            cur_result.append(r)
            return cur_result

        final_res = []
        for r in start_with(s):
            final_res.append(" ".join(r))
        return final_res