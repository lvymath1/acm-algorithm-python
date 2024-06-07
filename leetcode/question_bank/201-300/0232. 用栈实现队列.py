class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if not self.st2:
            self.prot()
        x = self.st2.pop()
        return x

    def peek(self) -> int:
        if not self.st2:
            self.prot()
        return self.st2[-1]

    def prot(self) -> None:
        while self.st1:
            x = self.st1.pop()
            self.st2.append(x)

    def empty(self) -> bool:
        if self.st1 or self.st2:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()