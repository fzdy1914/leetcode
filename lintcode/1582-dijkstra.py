def min_path_sum_i_i(self, matrix) -> int:
    def minimum(d):
        m = 99999999999

        for k, v in d.items():
            if v < m:
                m = v
                p = k
        return p, m

    # Write your code here

    n = len(matrix)
    m = len(matrix[0])
    to_check = dict()
    to_check[(n - 1, 0)] = matrix[n - 1][0]

    seen = set()

    while True:
        pos, s = minimum(to_check)
        if pos[0] == 0 and pos[1] == m - 1:
            return s
        del to_check[pos]
        seen.add(pos)

        choices = []
        if pos[0] > 0:
            choices.append((pos[0] - 1, pos[1]))
        if pos[0] < n - 1:
            choices.append((pos[0] + 1, pos[1]))
        if pos[1] > 0:
            choices.append((pos[0], pos[1] - 1))
        if pos[1] < m - 1:
            choices.append((pos[0], pos[1] + 1))

        for c in choices:
            if c in seen:
                continue
            new = s + matrix[c[0]][c[1]]
            if c in to_check:
                old = to_check[c]
                if new < old:
                    to_check[c] = new
            else:
                to_check[c] = new
