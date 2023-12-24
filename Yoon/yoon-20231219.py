class MyQueue:

    def __init__(self):
        self.__push_stack = []
        self.__pop_stack = []

    def push(self, x: int) -> None:
        self.__push_stack.append(x)

    def pop(self) -> int:
        if self.__pop_stack:
            return self.__pop_stack.pop()
        else:
            while self.__push_stack:
                temp = self.__push_stack.pop()
                self.__pop_stack.append(temp)
            return self.__pop_stack.pop()

    def peek(self) -> int:
        if self.__pop_stack:
            return self.__pop_stack[-1]
        else:
            while self.__push_stack:
                temp = self.__push_stack.pop()
                self.__pop_stack.append(temp)
            return self.__pop_stack[-1]

    def empty(self) -> bool:
        return False if self.__push_stack or self.__pop_stack else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()