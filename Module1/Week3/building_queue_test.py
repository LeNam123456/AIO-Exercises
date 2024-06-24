class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []
    def is_empty(self):
        if len(self.__queue) == 0: return True  
    def is_full(self):
        if len(self.__queue) == self.__capacity:
            print("Enough")
            return True
        else:
            return False
    def enqueue(self, element):
        if self.is_full() != True: return self.__queue.append(element)
        
    def dequeue(self):
        if self.is_empty() != 0: return (self.__queue.pop(0))
        
    def front(self):
        return self.__queue[0]

queue1 = Queue ( capacity =5)
queue1 . enqueue (1)
queue1 . enqueue (2)

print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())      
print(queue1.front())
print(queue1.dequeue()) 
print(queue1.is_empty())      