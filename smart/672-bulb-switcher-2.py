class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        d = dict()
        d[1] = [[1,1,1,1,1,1], [1,0,1,0,1,0], [0,1,0,1,0,1], [1,0,0,1,0,0]]
        d[2] = [
            [1,1,1,1,1,1],
            [1,0,1,0,1,0],
            [0,1,0,1,0,1],
            [0,1,1,0,1,1],
            [0,0,0,0,0,0],
            [0,0,1,1,1,0],
            [1,1,0,0,0,1]]
        d[3] = [
            [1,1,1,1,1,1],
            [1,0,1,0,1,0],
            [0,1,0,1,0,1],
            [1,0,0,1,0,0],
            [0,1,1,0,1,1],
            [0,0,0,0,0,0],
            [0,0,1,1,1,0],
            [1,1,0,0,0,1]]

        if presses > 3:
            presses = 3

        r = d[presses]

        s = set()
        for rr in r:
            rr.extend(rr.copy())

            s.add(tuple(rr[:(n%12)]))
        return len(s)
