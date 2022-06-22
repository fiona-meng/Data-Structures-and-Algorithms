from LinkedBinaryTree import LinkedBinaryTree


def min_and_max(bin_tree):
    if bin_tree.size == 0:
        raise Exception("Tree is empty")
    else:
        return subtree_min_and_max(bin_tree.root)


def subtree_min_and_max(root):
    if root.left is None and root.right is None:
        return root.data, root.data
    elif root.left is not None and root.right is None:
        left_min, left_max = subtree_min_and_max(root.left)
        return min(left_min, root.data), max(left_max, root.data)
    elif root.left is None and root.right is not None:
        right_min, right_max = subtree_min_and_max(root.right)
        return min(right_min, root.data), max(right_max, root.data)
    else:
        left_min, left_max = subtree_min_and_max(root.left)
        right_min, right_max = subtree_min_and_max(root.right)
        return min(left_min, right_min, root.data), max(left_max, right_max, root.data)



l_ch1 = LinkedBinaryTree.Node(5)
r_ch1 = LinkedBinaryTree.Node(1)
l_ch2 = LinkedBinaryTree.Node(9, l_ch1, r_ch1)
r1 = LinkedBinaryTree.Node(2, l_ch2, None)
ll_ch1 = LinkedBinaryTree.Node(8)
rr_ch1 = LinkedBinaryTree.Node(4)
r2 = LinkedBinaryTree.Node(7, ll_ch1, rr_ch1)
r = LinkedBinaryTree.Node(3, r1, r2)
tree = LinkedBinaryTree(r)

l_ch1 = LinkedBinaryTree.Node(5)
r_ch1 = LinkedBinaryTree.Node(1)
l_ch2 = LinkedBinaryTree.Node(9, None, l_ch1)
tree2 = LinkedBinaryTree(l_ch2)
print(min_and_max(tree2))