import time


def min_path_sum_i_i(matrix) -> int:
    # Write your code here
    result = []

    n = len(matrix)
    m = len(matrix[0])

    def search(pos, score, seen):
        new_score = matrix[pos[0]][pos[1]] + score
        if pos[0] == 0 and pos[1] == m - 1:
            result.append(new_score)
            return

        seen.add(pos)
        choise = []
        if pos[0] > 0:
            choise.append((pos[0] - 1, pos[1]))
        if pos[0] < n - 1:
            choise.append((pos[0] + 1, pos[1]))
        if pos[1] > 0:
            choise.append((pos[0], pos[1] - 1))
        if pos[1] < m - 1:
            choise.append((pos[0], pos[1] + 1))

        for c in choise:
            if c in seen:
                continue
            search(c, new_score, seen.copy())

    search((n - 1, 0), 0, set())
    return min(result)

m = [[2,3], [3,2]]
print(min_path_sum_i_i(m))