from LinkedBinaryTree_note import LinkedBinaryTree
from ArrayQueue import ArrayQueue


def bt_even_sum(root):
    def subtree_even_sum(sub_root):
        if sub_root is None:
            return 0
        else:
            left_count = subtree_even_sum(sub_root.left)
            right_count = subtree_even_sum(sub_root.right)
            if sub_root.data % 2 == 0:
                return left_count + right_count + sub_root.data
            else:
                return left_count + right_count
    return subtree_even_sum(root)


def bt_contains(root, val):
    def subtree_bt_contains(sub_root, n):
        if sub_root is None:
            return False
        else:
            left_contain = subtree_bt_contains(sub_root.left, n)
            right_contain = subtree_bt_contains(sub_root.right, n)
            return (sub_root.data == n) or left_contain or right_contain
    return subtree_bt_contains(root, val)


def add_bts(root1, root2):
    def merge(t1, t2):
        if not t1 and not t2:
            return None
        if t1 and t2:
            t3 = LinkedBinaryTree.Node(t1.data + t2.data)
            t3.left = merge(t1.left, t2.left)
            t3.right = merge(t1.right, t2.right)
            return t3
        elif t1:  # t2 is none
            t3 = LinkedBinaryTree.Node(t1.data)
            t3.left = merge(t1.left, None)
            t3.right = merge(t1.right, None)
            return t3

        elif t2:
            t3 = LinkedBinaryTree.Node(t2.data)
            t3.left = merge(None, t2.left)
            t3.right = merge(None, t2.right)
            return t3
    return merge(root1, root2)



l_ch1 = LinkedBinaryTree.Node(1)
r_ch1 = LinkedBinaryTree.Node(6)
r_ch2 = LinkedBinaryTree.Node(2, l_ch1, r_ch1)
l_ch2 = LinkedBinaryTree.Node(4)
r = LinkedBinaryTree.Node(5, l_ch2, r_ch2)

ll_ch1 = LinkedBinaryTree.Node(1)
rr_ch1 = LinkedBinaryTree.Node(6)
rr_ch2 = LinkedBinaryTree.Node(2, ll_ch1, rr_ch1)
ll_ch2 = LinkedBinaryTree.Node(4)
rr = LinkedBinaryTree.Node(6, ll_ch2, rr_ch2)
# print(bt_even_sum(r))
# print(bt_contains(r, 11))
print(add_bts(r, rr).data)


def invert_bt_rec(root):
    if root is None:
        return None
    invert_bt_rec(root.left)
    invert_bt_rec(root.right)
    root.left, root.right = root.right, root.left


def invert_bt(root):
    queue = ArrayQueue()
    queue.enqueue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        node.left, node.right = node.right, node.left
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

