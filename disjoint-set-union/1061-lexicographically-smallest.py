class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # class DSU:
        #     def __init__(self, N):
        #         self.root = [i for i in range(N)]

        #     def find(self, k):
        #         if self.root[k] == k:
        #             return k
        #         self.root[k] = self.find(self.root[k])
        #         return self.root[k]

        #     def union(self, a, b):
        #         x = self.find(a)
        #         y = self.find(b)
        #         if x < y:
        #             self.root[y] = x
        #         else:
        #             self.root[x] = y
        #         return

        # u = DSU(ord('z') + 1)

        # for i in range(len(s1)):
        #     u.union(ord(s1[i]), ord(s2[i]))

        # d = ""
        # for b in baseStr:
        #     d += chr(u.find(ord(b)))

        # return d

        class DSU:
            def __init__(self):
                self.root = dict()

            def find(self, k):
                if k not in self.root:
                    self.root[k] = k
                    return k
                if self.root[k] == k:
                    return k
                self.root[k] = self.find(self.root[k])
                return self.root[k]

            def union(self, a, b):
                x = self.find(a)
                y = self.find(b)
                if x < y:
                    self.root[y] = x
                else:
                    self.root[x] = y
                return

        u = DSU()

        for i in range(len(s1)):
            u.union(s1[i], s2[i])

        d = ""
        for b in baseStr:
            d += u.find(b)

        return d
