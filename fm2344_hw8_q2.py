from BinarySearchTreeMap import BinarySearchTreeMap


# 2a
def create_chain_bst(n):
    tree = BinarySearchTreeMap()
    for i in range(1, n+1):
        tree[i] = None
    return tree


# 2b
def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


def add_items(bst, low, high):
    if low == high:
        bst[high] = None
    else:
        mid = (high + low) // 2
        bst[mid] = None
        add_items(bst, low, mid - 1)
        add_items(bst, mid + 1, high)



# for i in create_complete_bst(7):
#     print(i)


# my_tree = create_chain_bst(4)
# for i in my_tree:
#     print(i)
