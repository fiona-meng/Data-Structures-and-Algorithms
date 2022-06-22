from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        for i in orig_str:
            if len(self.data) == 0:
                self.data.add_last((i, 1))
            elif self.data.trailer.prev.data[0] == i:
                curr = self.data.trailer.prev.data[-1]
                curr += 1
                self.data.delete_last()
                self.data.add_last((i, curr))
            else:
                self.data.add_last((i, 1))

    def __add__(self, other):
        if len(self.data) == 0 and len(other.data) == 0:
            return self
        if len(self.data) == 0:
            add_result = CompactString('')
            curr = other.data.header
            for i in range(len(other.data)):
                curr = curr.next
                add_result.data.add_last(curr.data)
        elif len(other.data) == 0:
            add_result = CompactString('')
            curr = self.data.header
            for i in range(len(self.data)):
                curr = curr.next
                add_result.data.add_last(curr.data)
        else:
            add_result = CompactString('')
            curr = self.data.header
            for i in range(len(self.data)):
                curr = curr.next
                add_result.data.add_last(curr.data)
            if add_result.data.trailer.prev.data[0] == other.data.header.next.data[0]:
                letter = add_result.data.trailer.prev.data[0]
                n = add_result.data.trailer.prev.data[1] + other.data.header.next.data[1]
                add_result.data.delete_last()
                add_result.data.add_last((letter, n))

                curr = other.data.header.next
                for i in range(len(other.data) - 1):
                    curr = curr.next
                    add_result.data.add_last(curr.data)
            else:
                curr = other.data.header
                for i in range(len(other.data)):
                    curr = curr.next
                    add_result.data.add_last(curr.data)

        return add_result

    def __lt__(self, other):
        if self.data == other.data:
            return False
        self_curr = self.data.header.next
        other_curr = other.data.header.next
        while True:
            if len(self.data) == 0 and len(other.data) == 0:
                return False
            elif len(self.data) != 0 and len(other.data) == 0:
                return False
            elif len(self.data) == 0 and len(other.data) != 0:
                return True
            else:
                if ord(self_curr.data[0]) < ord(other_curr.data[0]):
                    return True
                elif ord(self_curr.data[0]) > ord(other_curr.data[0]):
                    return False
                else:
                    if self_curr.data[1] == other_curr.data[1]:
                        self_curr = self_curr.next
                        other_curr = other_curr.next
                    elif self_curr.data[1] > other_curr.data[1]:
                        other_curr = other_curr.next
                    else:
                        self_curr = self_curr.next


    def __le__(self, other):
        if self.data == other.data:
            return True
        self_curr = self.data.header.next
        other_curr = other.data.header.next
        while True:
            if len(self.data) == 0 and len(other.data) == 0:
                return True
            elif len(self.data) != 0 and len(other.data) == 0:
                return False
            elif len(self.data) == 0 and len(other.data) != 0:
                return True
            else:
                if ord(self_curr.data[0]) < ord(other_curr.data[0]):
                    return True
                elif ord(self_curr.data[0]) > ord(other_curr.data[0]):
                    return False
                else:
                    if self_curr.data[1] == other_curr.data[1]:
                        self_curr = self_curr.next
                        other_curr = other_curr.next
                    elif self_curr.data[1] > other_curr.data[1]:
                        other_curr = other_curr.next
                    else:
                        self_curr = self_curr.next


    def __gt__(self, other):
        if self.data == other.data:
            return False
        self_curr = self.data.header.next
        other_curr = other.data.header.next
        while True:
            if len(self.data) == 0 and len(other.data) == 0:
                return False
            elif len(self.data) != 0 and len(other.data) == 0:
                return True
            elif len(self.data) == 0 and len(other.data) != 0:
                return False
            else:
                if ord(self_curr.data[0]) < ord(other_curr.data[0]):
                    return False
                elif ord(self_curr.data[0]) > ord(other_curr.data[0]):
                    return True
                else:
                    if self_curr.data[1] == other_curr.data[1]:
                        self_curr = self_curr.next
                        other_curr = other_curr.next
                    elif self_curr.data[1] > other_curr.data[1]:
                        other_curr = other_curr.next
                    else:
                        self_curr = self_curr.next


    def __ge__(self, other):
        if self.data == other.data:
            return True
        self_curr = self.data.header.next
        other_curr = other.data.header.next
        while True:
            if len(self.data) == 0 and len(other.data) == 0:
                return True
            elif len(self.data) != 0 and len(other.data) == 0:
                return True
            elif len(self.data) == 0 and len(other.data) != 0:
                return False
            else:
                if ord(self_curr.data[0]) < ord(other_curr.data[0]):
                    return False
                elif ord(self_curr.data[0]) > ord(other_curr.data[0]):
                    return True
                else:
                    if self_curr.data[1] == other_curr.data[1]:
                        self_curr = self_curr.next
                        other_curr = other_curr.next
                    elif self_curr.data[1] > other_curr.data[1]:
                        other_curr = other_curr.next
                    else:
                        self_curr = self_curr.next

    def __repr__(self):
        exp = ''
        curr = self.data.header
        for i in self.data:
            curr = curr.next
            letter = curr.data[0]
            n = curr.data[1]
            exp += letter * n
        return exp


s1 = CompactString('aaaaabbbaaac')
s2 = CompactString('aaaaaaacccaaaa')
s4 = CompactString('')
s5 = CompactString('')
s3 = s2 + s1
print(s4 > s1)
# print(s3.data.trailer.prev.prev.data)
# print(s3)
# print(s1 < s2)
# print('aaaaabbbaaac' >= 'aaaaaaacccaaaa')

