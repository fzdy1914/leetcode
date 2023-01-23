from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        mem = dict()
        def generate(n):
            if n in mem:
                return mem[n]

            if n == 1:
                mem[1] = ["()"]
                return ["()"]

            result = set()
            m1 = generate(n - 1)

            for m in m1:
                result.add("(" + m + ")")

            for i in range(1, n):
                l = generate(i)
                r = generate(n - i)

                for ll in l:
                    for rr in r:
                        result.add(ll + rr)

            r =  list(result)
            mem[n] = r
            return r

        return generate(n)