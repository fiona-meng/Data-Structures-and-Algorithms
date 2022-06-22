from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    if prefix_exp_str == "":
        raise Exception("Tree is Empty")
    prefix_exp_lst = prefix_exp_str.split()
    operations = "+-*/"
    def create_expression_tree_helper(prefix_exp, start_pos):
        if prefix_exp[start_pos] in operations:
            left_sub, left_size = create_expression_tree_helper(prefix_exp, start_pos + 1)
            right_sub, right_size = create_expression_tree_helper(prefix_exp, start_pos + 1 + left_size)
            sub_root = LinkedBinaryTree.Node(str(prefix_exp[start_pos]), left_sub, right_sub)
            return sub_root, 1 + left_size + right_size
        else:
            new_node = LinkedBinaryTree.Node(int(prefix_exp_lst[start_pos]))
            return new_node, 1
    result_tree, size = create_expression_tree_helper(prefix_exp_lst, 0)
    return LinkedBinaryTree(result_tree)


def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    def prefix_to_postfix_helper(root):
        if root.left is None and root.right is None:
            return str(root.data)
        else:
            return prefix_to_postfix_helper(root.left) + " " + prefix_to_postfix_helper(root.right) + " " + root.data
    return str(prefix_to_postfix_helper(tree.root))




l_ch1 = LinkedBinaryTree.Node(15)
r_ch1 = LinkedBinaryTree.Node(6)
l_ch2 = LinkedBinaryTree.Node('-', l_ch1, r_ch1)
ll_ch1 = LinkedBinaryTree.Node(4)
r1 = LinkedBinaryTree.Node('+', l_ch2, ll_ch1)
rr_ch1 = LinkedBinaryTree.Node(2)
r = LinkedBinaryTree.Node("*", rr_ch1, r1)
tree = LinkedBinaryTree(r)
# x = create_expression_tree('* 2 + - 15 6 4')
# y = create_expression_tree('')
# print(x.root.right.left.data)
# print(y.root)
# print(prefix_to_postfix('* 2 + - 15 6 4'))
# print(prefix_to_postfix(''))