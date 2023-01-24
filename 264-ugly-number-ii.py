import queue


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        visited = {1}
        q = queue.PriorityQueue()
        count = 0
        q.put(1)

        while not q.empty():
            c = q.get()
            count += 1
            if count == n:
                return c

            cs = [c * 2, c * 3, c * 5]

            for cc in cs:
                if cc not in visited:
                    q.put(cc)
                    visited.add(cc)
