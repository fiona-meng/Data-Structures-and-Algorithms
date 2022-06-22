from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in num_str:
            self.data.add_last(i)

    def __add__(self, other):
        result_Integer = Integer('')
        self_curr = self.data.trailer
        other_curr = other.data.trailer
        previous = 0
        while True:
            if self_curr == self.data.header.next and other_curr == other.data.header.next and previous == 0:
                result_curr = result_Integer.data.header.next
                for i in range(len(result_Integer.data) - 1):
                    if result_curr.data == '0' and result_curr.next.data != '0':
                        result_Integer.data.delete_first()
                        return result_Integer
                    elif result_curr.data == '0' and result_curr.next.data == '0':
                        result_curr = result_curr.next
                        result_Integer.data.delete_first()

                return result_Integer
            elif self_curr == self.data.header.next and other_curr == other.data.header.next and previous != 0:
                result_Integer.data.add_first(str(previous))
                result_curr = result_Integer.data.header.next
                for i in range(len(result_Integer.data) - 1):
                    if result_curr.data == '0' and result_curr.next.data != '0':
                        result_Integer.data.delete_first()
                        return result_Integer
                    elif result_curr.data == '0' and result_curr.next.data == '0':
                        result_curr = result_curr.next
                        result_Integer.data.delete_first()

                return result_Integer
            elif self_curr == self.data.header.next and other_curr != other.data.header.next:
                other_curr = other_curr.prev
                curr = str(int(other_curr.data) + int(previous))
                result_Integer.data.add_first(curr[-1])
                if len(curr) == 1:
                    previous = 0
                else:
                    previous = curr[0]
            elif self_curr != self.data.header.next and other_curr == other.data.header.next:
                self_curr = self_curr.prev
                curr = str(int(self_curr.data) + int(previous))
                result_Integer.data.add_first(curr[-1])
                if len(curr) == 1:
                    previous = 0
                else:
                    previous = curr[0]
            else:
                self_curr = self_curr.prev
                other_curr = other_curr.prev
                curr = str(int(self_curr.data) + int(other_curr.data) + int(previous))
                result_Integer.data.add_first(curr[-1])
                if len(curr) == 1:
                    previous = 0
                else:
                    previous = curr[0]

    def __repr__(self):
        repr_result = ""
        curr = self.data.header
        for i in range(len(self.data)):
            curr = curr.next
            repr_result = repr_result + curr.data
        return repr_result



n1 = Integer('00009999991')
n2 = Integer('20')
n3 = n2 + n1
# print(n1)
# print(n2)
# print(n3)



