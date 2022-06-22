from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    result_lst = DoublyLinkedList()
    curr = lnk_lst.header
    while curr.next != lnk_lst.trailer:
        curr = curr.next
        result_lst.add_last(curr.data)
    return result_lst


# lnk_lst1 = DoublyLinkedList()
# elem1 = DoublyLinkedList()
# elem1.add_last(1)
# elem1.add_last(2)
# lnk_lst1.add_last(elem1)
# elem2 = 3
# lnk_lst1.add_last(elem2)
#
# lnk_lst2 = copy_linked_list(lnk_lst1)
# e1 = lnk_lst1.header.next
# e1_1 = e1.data.header.next
# e1_1.data = 10
# e2 = lnk_lst2.header.next
# e2_1 = e2.data.header.next
# print(e2_1.data)


def deep_copy_linked_list(lnk_lst):
    result_lst = DoublyLinkedList()
    curr = lnk_lst.header
    while curr.next != lnk_lst.trailer:
        curr = curr.next
        if isinstance(curr.data, int):
            result_lst.add_last(curr.data)
        else:
            result_lst.add_last(deep_copy_linked_list(curr.data))
    return result_lst


# lnk_lst1 = DoublyLinkedList()
# elem1 = DoublyLinkedList()
# elem1.add_last(1)
# elem1.add_last(2)
# lnk_lst1.add_last(elem1)
# elem2 = 3
# lnk_lst1.add_last(elem2)
#
# lnk_lst2 = deep_copy_linked_list(lnk_lst1)
# e1 = lnk_lst1.header.next
# e1_1 = e1.data.header.next
# e1_1.data = 10
# e2 = lnk_lst2.header.next
# e2_1 = e2.data.header.next
# print(e2_1.data)