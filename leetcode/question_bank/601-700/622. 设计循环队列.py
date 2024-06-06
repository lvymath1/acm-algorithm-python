class MyCircularQueue:

    def __init__(self, k: int):
        self.n = k
        self.q = [0] * k
        self.left, self.right = 0, 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.right] = value
        self.right = (self.right + 1) % self.n
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left = (self.left + 1) % self.n
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.right - 1) % self.n]


    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.n:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()