class MinStack:

    def __init__(self):
        self.st = []
        self.mn = []


    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.mn or val < self.mn[-1]:
            self.mn.append(val)
        else:
            self.mn.append(self.mn[-1])


    def pop(self) -> None:
        self.mn.pop()
        return self.st.pop()


    def top(self) -> int:
        return self.st[-1]


    def getMin(self) -> int:
        return self.mn[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()