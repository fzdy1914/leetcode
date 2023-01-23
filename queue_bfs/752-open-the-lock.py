from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def generate(number):
            rs = []
            temp = [int(c) for c in number]

            for i in range(4):
                temp[i] = (temp[i] + 1) % 10
                tt = [str(t) for t in temp]
                rs.append("".join(tt))
                temp[i] = (temp[i] - 2) % 10
                tt = [str(t) for t in temp]
                rs.append("".join(tt))
                temp[i] = (temp[i] + 1) % 10

            return rs

        q = [("0000", 0)]
        visited = {"0000"}
        deadends = set(deadends)

        while len(q) > 0:
            node = q.pop(0)
            next_step = node[1] + 1

            if node[0] == target:
                return node[1]

            if node[0] in deadends:
                continue

            for possible in generate(node[0]):
                if possible in visited:
                    continue

                visited.add(possible)
                q.append((possible, next_step))

        return -1
