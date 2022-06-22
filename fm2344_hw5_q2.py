from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def push(self, val):
        if (self.is_empty()):
            x = (val, val)
            self.data.push(x)
        else:
            last_element = self.data.top()
            current_max = last_element[1]
            if current_max > val:
                x = (val, current_max)
                self.data.push(x)
            else:
                x = (val, val)
                self.data.push(x)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.top()[0]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        else:
            x = self.data.top()[0]
            self.data.pop()
            return x

    def max(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        else:
            return self.data.top()[1]

maxS = MaxStack()
print(maxS.is_empty())
maxS.push(3)
print(maxS.is_empty())
print(len(maxS))
maxS.push(1)
maxS.push(6)
maxS.push(4)
print(len(maxS))
print(maxS.max())
print(maxS.pop())
print(maxS.pop())
print(maxS.max())
