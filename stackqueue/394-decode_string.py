class Solution:
    def decodeString(self, s: str) -> str:
        number_stack = []
        string_stack = []

        i = 0
        while i < len(s):
            if s[i].isnumeric():
                j = i + 1
                while s[j].isnumeric():
                    j += 1
                number_stack.append(s[i:j])
                i = j
                continue
            if s[i] == "[":
                string_stack.append("")
                i += 1
                continue
            if s[i] == "]":
                i += 1
                ss = string_stack.pop()
                times = number_stack.pop()
                times = int(times)

                ss = times * ss
                if len(string_stack) != 0:
                    string_stack[-1] = string_stack[-1] + ss
                else:
                    string_stack = [ss, ]
                continue

            if len(string_stack) != 0:
                string_stack[-1] = string_stack[-1] + s[i]
            else:
                string_stack = [s[i], ]
            i += 1
        return string_stack[0]

