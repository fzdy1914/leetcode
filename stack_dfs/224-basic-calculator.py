class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        def eval_1(lst):
            stack = []

            idx = 0
            while idx < len(lst):
                if lst[idx] == "+":
                    left = stack.pop()
                    stack.append(left + lst[idx + 1])
                    idx += 2
                elif lst[idx] == "-":
                    if len(stack) > 0 and type(stack[-1]) == int:
                        left = stack.pop()
                        stack.append(left - lst[idx + 1])
                    else:
                        stack.append(- lst[idx + 1])
                    idx += 2
                else:
                    stack.append(lst[idx])
                    idx += 1
            return stack[0]


        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] == ")":
                temp = []
                while True:
                    cc = stack.pop()
                    if cc == "(":
                        break
                    temp.insert(0, cc)

                stack.append(eval_1(temp))

                idx += 1
                continue

            if s[idx].isnumeric():
                end = idx + 1
                while end < len(s) and s[end].isnumeric():
                    end += 1
                c = int(s[idx:end])
                idx = end
                stack.append(c)
                continue

            stack.append(s[idx])
            idx += 1

        return eval_1(stack)