class MyQueue:
    

    def __init__(self):
        self = []
   

    def push(self, x: int) -> None:
        self.append(x)

        
    def pop(self) -> int:
        fst = self[0]
        return fst
        

    def peek(self) -> int:
        return self[0]
        

    def empty(self) -> bool:
        if len(self) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()