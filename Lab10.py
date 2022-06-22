from DoublyLinkedList import DoublyLinkedList


# Coding 1
class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.add_last(val)

    def top(self):
        if self.is_empty():
            raise Exception("the stack is empty")
        return self.data.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise Exception("the stack is empty")
        return self.data.delete_last()


# 2
def __getitem__(self, i):
    # if index is in first half, start from header
    if 0 <= i <= len(self) // 2:
        start = self.header.next
        for i in range(i):
            start = start.next
        return start.data
    elif len(self) // 2 < i < len(self):  # if index in second half, start from trailer
        start = self.trailer.prev
        for i in range(len(self) - 1, i, -1):
            start = start.prev
        return start.data
    else:
        raise IndexError("Index out of range")


# 3
class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.data.add_last(e)
        if len(self) == 1: # only one element
            self.mid = self.data.trailer.prev # mid is last node
        elif len(self) % 2 != 0: # if len is odd, bump pointer up
            self.mid = self.mid.next

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        val = self.data.delete_last()
        if self.is_empty():
            self.mid = None
        elif len(self) % 2 == 0:
            self.mid = self.mid.prev
        return val

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.data.trailer.prev.data

    def mid_push(self, e):
        self.data.add_after(self.mid, e)
        if len(self) == 1:
            self.mid = self.data.trailer.prev
        elif len(self) % 2 != 0:
            self.mid = self.mid.next

    def get_mid(self):
        return self.mid.data


# 4
class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.header = SinglyLinkedList.Node()
        self.size = 0
        self.last = self.header

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def add_after(self, node, val):
        if node == self.last:
            self.add_last(val)
        else:
            new_node = SinglyLinkedList(val)
            new_node.next = node.next
            node.next = new_node
            self.size += 1
            return new_node

    def add_before(self, node, val):
        curr = self.header
        while curr.next is not node:
            curr = curr.next
        new_node = SinglyLinkedList(val)
        curr.next = new_node
        new_node.next = node
        self.size += 1
        return new_node

    def add_first(self, val):
        node = self.add_after(self.header, val)
        if len(self) == 1:
            self.last = node
        return node

    def add_last(self, val):
        self.last = self.add_after(self.last, val)
        return self.last

    def delete_node(self, node):
        if node == self.last:
            self.delete_last()
        else:
            curr = self.header
            while curr.next is not node:
                curr = curr.next
            curr.next = node.next
            self.size -= 1
            val = node.data
            node.disconnect()
            return val

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        curr = self.header
        while curr.next is not self.last:
            curr = curr.next
        val = self.delete_node(self.last)
        self.last = curr
        return val

    def __iter__(self):
        cursor = self.header.next
        while cursor is not None:
            yield cursor.data
            cursor = cursor.nxt

    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self]) + "]"