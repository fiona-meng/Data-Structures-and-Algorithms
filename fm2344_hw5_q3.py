from ArrayDeque import ArrayDeque
from ArrayStack import ArrayStack


class MidStack:
    def __init__(self):
        self.data_stack = ArrayStack()
        self.data_deque = ArrayDeque()

    def is_empty(self):
        return self.data_stack.is_empty() and self.data_deque.is_empty()

    def __len__(self):
        return len(self.data_stack) + len(self.data_deque)

    def push(self, val):
        self.data_deque.enqueue_last(val)
        if len(self.data_deque) > len(self.data_stack):
            self.data_stack.push(self.data_deque.dequeue_first())

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data_deque.last()

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        if len(self.data_deque) < len(self.data_stack):
            self.data_deque.enqueue_first(self.data_stack.pop())
        return self.data_deque.dequeue_last()

    def mid_push(self, val):
        self.data_stack.push(val)

# midS = MidStack()
# midS.push(2)
# midS.push(4)
# midS.push(6)
# midS.push(8)
# midS.push(10)
# midS.mid_push(10)
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())
# print(midS.pop())

