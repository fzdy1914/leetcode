# TODO
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_op(a):
            return a == "+" or a == "-" or a == "*" or a == "/"
        stack = []
        for op in tokens:
            if not is_op(op):
                stack.append(int(op))
            else:
                second = stack.pop()
                first = stack.pop()

                if op == "+":
                    stack.append(first + second)
                if op == "-":
                    stack.append(first - second)
                if op == "*":
                    stack.append(first * second)
                if op == "/":
                    stack.append(int(first / second))
        return stack[0]