from BinarySearchTreeMap import BinarySearchTreeMap


def find_min_abs_difference(bst):
    lst = []
    def find_min_abs_difference(lst, root):
        if root is None:
            pass
        else:
            find_min_abs_difference(lst, root.left)
            lst.append(root.item.key)
            find_min_abs_difference(lst, root.right)
    find_min_abs_difference(lst, bst.root)
    for i in range(len(lst) - 1):
        lst[i] = abs(lst[i] - lst[i + 1])
    return min(lst)


tree = BinarySearchTreeMap()
tree[9] = None
tree[7] = None
tree[4] = None
tree[1] = None
tree[6] = None
tree[20] = None
tree[17] = None
tree[25] = None
# print(tree.root)

# print(find_min_abs_difference(tree))



