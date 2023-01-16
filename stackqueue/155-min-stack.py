class MinStack:
    def __init__(self):
        self.min = []
        self.all = []

    def push(self, val: int) -> None:
        self.all.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        else:
            if val < self.min[-1]:
                self.min.append(val)
            else:
                self.min.append(self.min[-1])

    def pop(self) -> None:
        self.all.pop()
        self.min.pop()

    def top(self) -> int:
        return self.all[-1]

    def getMin(self) -> int:
        return self.min[-1]