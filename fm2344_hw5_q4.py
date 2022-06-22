from ArrayStack import ArrayStack

class Queue:
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()

    def __len__(self):
        return len(self.stack1)

    def is_empty(self):
        return len(self.stack1) == 0

    def enqueue(self, val):
        if self.stack1.is_empty() and self.stack2.is_empty():
            self.stack1.push(val)
        else:
            while not self.stack1.is_empty():
                x = self.stack1.pop()
                self.stack2.push(x)
            self.stack1.push(val)
            while not self.stack2.is_empty():
                y = self.stack2.pop()
                self.stack1.push(y)


    def dequeue(self):
        if self.stack1.is_empty():
            raise Exception("Queue is Empty")
        front = self.stack1.top()
        self.stack1.pop()
        return front

    def first(self):
        return self.stack1.top()


# q1 = Queue()
# q1.enqueue(1)
# q1.enqueue(2)
# q1.enqueue(3)
# q1.enqueue(4)
# print(q1.first())
# q1.dequeue()
# q1.dequeue()
# print(q1.first())
# q1.dequeue()
# print(q1.first())