from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operator_idx = []
        for i in range(len(expression)):
            if expression[i] in ["+", "-", "*"]:
                operator_idx.append(i)

        if len(operator_idx) == 0:
            return [int(expression)]

        rs = []
        for i in operator_idx:
            left_ans = self.diffWaysToCompute(expression[:i])
            right_ans = self.diffWaysToCompute(expression[i + 1:])
            for l in left_ans:
                for r in right_ans:
                    if expression[i] == "+":
                        rs.append(l + r)
                    if expression[i] == "-":
                        rs.append(l - r)
                    if expression[i] == "*":
                        rs.append(l * r)

        return list(rs)