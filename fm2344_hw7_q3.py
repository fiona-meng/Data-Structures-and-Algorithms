from LinkedBinaryTree import LinkedBinaryTree


def is_height_balanced(bin_tree):
    def is_height_balanced_helper(root):
        if root.left is None and root.right is None:
            return 1, True
        elif root.left is not None and root.right is None:
            val, balanced = is_height_balanced_helper(root.left)
            return val + 1, val <= 1 and balanced
        elif root.left is None and root.right is not None:
            val, balanced = is_height_balanced_helper(root.right)
            return val + 1, val <= 1 and balanced
        else:
            val_l, balanced_l = is_height_balanced_helper(root.left)
            val_r, balanced_r = is_height_balanced_helper(root.right)
            return max(val_l, val_r) + 1, balanced_r and balanced_l and abs(val_l - val_r) <= 1
    val, balanced = is_height_balanced_helper(bin_tree.root)
    return balanced


# l_ch1 = LinkedBinaryTree.Node(5)
# r_ch1 = LinkedBinaryTree.Node(1)
# l_ch2 = LinkedBinaryTree.Node(9, l_ch1, r_ch1)
# r1 = LinkedBinaryTree.Node(2, l_ch2, None)
# ll_ch1 = LinkedBinaryTree.Node(8)
# rr_ch1 = LinkedBinaryTree.Node(4)
# r2 = LinkedBinaryTree.Node(7, ll_ch1, rr_ch1)
# r = LinkedBinaryTree.Node(3, r1, r2)
# tree = LinkedBinaryTree(r)
# print(is_height_balanced(tree))

l_ch1 = LinkedBinaryTree.Node(5)
r_ch1 = LinkedBinaryTree.Node(1)
l_ch2 = LinkedBinaryTree.Node(8, l_ch1, r_ch1)
r_ch2 = LinkedBinaryTree.Node(4, None, None)
r1 = LinkedBinaryTree.Node(7, l_ch2, r_ch2)
ll_ch1 = LinkedBinaryTree.Node(9)
r2 = LinkedBinaryTree.Node(2, ll_ch1, None)
r = LinkedBinaryTree.Node(3, r2, r1)
tree = LinkedBinaryTree(r)
print(is_height_balanced(tree))