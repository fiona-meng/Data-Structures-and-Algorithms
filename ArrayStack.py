# from ArrayList import ArrayList
#
#
# class ArrayStack:
#     def __init__(self):
#         self.data = ArrayList()
#
#     def __len__(self):
#         return len(self.data)
#
#     def is_empty(self):
#         return len(self) == 0
#
#     def push(self, item):
#         self.data.append(item)
#
#     def pop(self):
#         if self.is_empty():
#             raise Exception("Stack is Empty")
#         return self.data.pop()
#
#     def top(self):
#         if self.is_empty():
#             raise Exception("Stack is Empty")
#         return self.data[-1]

from ArrayList import ArrayList

class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()
