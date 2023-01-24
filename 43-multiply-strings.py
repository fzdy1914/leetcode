class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = [int(c) for c in num1[::-1]]
        b = [int(c) for c in num2[::-1]]

        result = [0] * (2 * max(len(a), len(b)))
        for i in range(len(a)):
            for j in range(len(b)):
                result[i + j] += a[i] * b[j]

        for i in range(len(result) - 1):
            result[i + 1] += result[i] // 10
            result[i] = result[i] % 10

        idx = len(result) - 1
        while idx >= 0 and result[idx] == 0:
            idx -= 1

        if idx == -1:
            return "0"

        return "".join([str(i) for i in reversed(result[:idx + 1])])
