from BinarySearchTreeMap import BinarySearchTreeMap


def restore_bst(prefix_lst):
    tree = BinarySearchTreeMap()
    restore_bst_helper(tree, prefix_lst, 0, len(prefix_lst) -1)
    return tree


def restore_bst_helper(tree, prefix, start, end):
    if start > end:
        return None
    else:
        tree[prefix[start]] = None
        curr = start
        while curr <= end:
            if prefix[curr] > prefix[start]:
                break
            curr += 1
        restore_bst_helper(tree, prefix, start + 1, curr - 1)
        restore_bst_helper(tree, prefix, curr, end)


# for i in restore_bst([9, 7, 3, 1, 5, 13, 11, 15]):
#     print(i)




