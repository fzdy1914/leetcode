class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0

        d = dict()
        result = 0
        while right < len(fruits):
            c = fruits[right]
            right += 1

            if c in d:
                d[c] += 1
            else:
                d[c] = 1

            while left < right:
                if len(d) <= 2:
                    r = 0
                    for k, v in d.items():
                        r += v
                    result = max(result, r)

                    break

                cc = fruits[left]

                if d[cc] == 1:
                    del d[cc]
                else:
                    d[cc] -= 1

                left += 1

        return result
