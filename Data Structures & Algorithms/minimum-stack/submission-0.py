class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_s=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_s or self.min_s[-1]>=val:
            self.min_s.append(val)
    def pop(self) -> None:
        if self.stack:
            char=self.stack.pop()
            if char<=self.min_s[-1]:
                self.min_s.pop()
        return char
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return null

    def getMin(self) -> int:
        return self.min_s[-1]
