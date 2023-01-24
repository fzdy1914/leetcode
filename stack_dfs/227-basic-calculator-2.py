class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        q = []
        idx = 0
        while idx < len(s):
            if s[idx].isnumeric():
                end = idx + 1
                while end < len(s) and s[end].isnumeric():
                    end += 1
                c = int(s[idx:end])
                idx = end
                q.append(c)
                continue
            q.append(s[idx])
            idx += 1

        stack = []
        idx = 0
        while idx < len(q):
            if q[idx] == "*":
                left = stack.pop()
                stack.append(left * q[idx + 1])
                idx += 2
            elif q[idx] == "/":
                left = stack.pop()
                stack.append(int(left / q[idx + 1]))
                idx += 2
            else:
                stack.append(q[idx])
                idx += 1

        q = stack
        stack = []
        idx = 0
        while idx < len(q):
            if q[idx] == "+":
                left = stack.pop()
                stack.append(left + q[idx + 1])
                idx += 2
            elif q[idx] == "-":
                left = stack.pop()
                stack.append(int(left - q[idx + 1]))
                idx += 2
            else:
                stack.append(q[idx])
                idx += 1

        return stack[0]