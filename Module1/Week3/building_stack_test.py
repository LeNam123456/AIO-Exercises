class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []
    def get_stack(self):
        return self.__stack
    def is_full(self):
        if len(self.__stack) == self.__capacity:
            return True
        else:
            return print('Still empty')

    def push(self, value):
        if self.is_full() == True:
            print('Enough')
        else:
            self.__stack.append(value)

    def top(self):
        return print(self.__stack[-1])
    def pop(self):
        return print(self.__stack.pop())
    def print(self):
        print(self.__stack)


stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)


stack1.top()
stack1.pop()
print(stack1.get_stack())