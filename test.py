from LinkedBinaryTree import LinkedBinaryTree


def parity_distribution(root):
    if root is None:
        return (0, 0)
    else:
        left_even, left_odd = parity_distribution(root.left)
        right_even, right_odd = parity_distribution(root.right)
        if root.data % 2 == 0:
            return left_even + right_even + 1, left_odd + right_odd
        else:
            return left_even + right_even, left_odd + right_odd + 1

l_ch1 = LinkedBinaryTree.Node(5)
r_ch1 = LinkedBinaryTree.Node(1)
l_ch2 = LinkedBinaryTree.Node(9, l_ch1, r_ch1)
r1 = LinkedBinaryTree.Node(2, l_ch2, None)
ll_ch1 = LinkedBinaryTree.Node(8)
rr_ch1 = LinkedBinaryTree.Node(4)
r2 = LinkedBinaryTree.Node(7, ll_ch1, rr_ch1)
r = LinkedBinaryTree.Node(3, r1, r2)
tree = LinkedBinaryTree(r)
tree1 = LinkedBinaryTree(None)
print(parity_distribution(r))