class MyQueue:

    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.append(x)
        
    def pop(self) -> int:
        x=self.lst[0]
        self.lst.pop(0)
        return x
        
    def peek(self) -> int:        
        return self.lst[0]

    def empty(self) -> bool:        
        if len(self.lst)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()