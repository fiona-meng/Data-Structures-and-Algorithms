from DoublyLinkedList import DoublyLinkedList


def insert_sorted(srt_lnk_lst, elem):
    ptr = srt_lnk_lst.header.next
    while ptr is not srt_lnk_lst.trailer and ptr.data < elem:
        ptr = ptr.next

    # adding before ptr here
    prev_node = ptr.prev
    next_node = ptr
    new_node = DoublyLinkedList.Node(elem)

    # set pointers to insert new node
    new_node.prev = prev_node
    new_node.next = next_node

    prev_node.next = new_node
    next_node.prev = new_node

    # update list size
    srt_lnk_lst.n += 1
    return srt_lnk_lst

n = DoublyLinkedList()
n.add_last(1)
n.add_last(3)
n.add_last(5)
n.add_last(7)
n.add_last(12)
# print(insert_sorted(n, 100))
lst = [1, 2, 3]
lst.extend([7,8])
print(lst)

# q5
from ArrayStack import ArrayStack


class DupStack:
    def __init__(self):
        self.s = ArrayStack()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        if self.is_empty():
            # Pushing "tuples" (2 element lists) into stack:
            #   [elem, count]
            self.s.push([e, 1])
        else:
            top_pair = self.s.top()
            # 2-elem list, not a tuple, so we can modify it
            if e == top_pair[0]:
                top_pair[1] += 1
            else:
                self.s.push([e, 1])
        self.n += 1

    def top(self):
        if self.is_empty():
            raise Exception("Empty DupStack")
        else:
            top_elem, top_count = self.s.top()
            return top_elem

    def top_dups_count(self):
        if self.is_empty():
            raise Exception("Empty DupStack")
        else:
            top_elem, top_count = self.s.top()
            return top_count

    def pop(self):
        if self.is_empty():
            raise Exception("Empty DupStack")
        else:
            top_pair = self.s.top()

            # if top_count == 1, remove pair altogether from stack
            if top_pair[1] == 1:
                self.s.pop()
            # if top_count > 1, update top_count of top element
            else:
                top_pair[1] -= 1

            self.n -= 1
            return top_pair[0]


    def pop_dups(self):
        if self.is_empty():
            raise Exception("Empty DupStack")
        else:
            pop_elem, pop_size = self.s.pop()
            self.n -= pop_size
            return pop_elem

