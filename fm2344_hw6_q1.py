from DoublyLinkedList import DoublyLinkedList


class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, val):
        self.data.add_last(val)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data.header.next.data
        self.data.delete_first()
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data.header.next.data

# LQ = LinkedQueue()
# LQ.enqueue(0)
# LQ.enqueue(1)
# LQ.enqueue(2)
# LQ.enqueue(3)
# LQ.enqueue(4)
# LQ.dequeue()
# LQ.dequeue()
# LQ.dequeue()
# LQ.dequeue()
# LQ.dequeue()
# print(LQ.first())
