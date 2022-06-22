from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(l1_curr, l2_curr):
        if l1_curr == srt_lnk_lst1.trailer and l2_curr == srt_lnk_lst2.trailer:
            return None
        elif l1_curr != srt_lnk_lst1.trailer and l2_curr == srt_lnk_lst2.trailer:
            while l1_curr != srt_lnk_lst1.trailer:
                result_lst.add_last(l1_curr.data)
                l1_curr = l1_curr.next
            return result_lst

        elif l1_curr == srt_lnk_lst1.trailer and l2_curr != srt_lnk_lst2.trailer:
            while l2_curr != srt_lnk_lst2.trailer:
                result_lst.add_last(l2_curr.data)
                l2_curr = l2_curr.next
            return result_lst

        else:
            if l1_curr.data == l2_curr.data:
                result_lst.add_last(l1_curr.data)
                result_lst.add_last(l2_curr.data)
                merge_sublists(l1_curr.next, l2_curr.next)
            elif l1_curr.data < l2_curr.data:
                result_lst.add_last(l1_curr.data)
                merge_sublists(l1_curr.next, l2_curr)
            elif l1_curr.data > l2_curr.data:
                result_lst.add_last(l2_curr.data)
                merge_sublists(l1_curr, l2_curr.next)
        return result_lst

    result_lst = DoublyLinkedList()
    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)

a = DoublyLinkedList()
a.add_last(1)
a.add_last(3)
a.add_last(5)
a.add_last(6)
a.add_last(8)
b = DoublyLinkedList()
b.add_last(2)
b.add_last(3)
b.add_last(5)
b.add_last(10)
b.add_last(15)
b.add_last(18)
# print(merge_linked_lists(a, b))



