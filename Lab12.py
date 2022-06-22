from BinarySearchTreeMap import BinarySearchTreeMap


def min_max_BST(bst):
    minimum = bst.root
    maximum = bst.root
    while minimum.left is not None:
        minimum = minimum.left

    while maximum.right is not None:
        maximum = maximum.right

    return(minimum.item.key, maximum.item.key)


def glt_n(root, n):
    curr = root
    gtln = -1

    while curr is not None:
        if n == curr.item.key:
            return curr.item.key

        if n > curr.item.key:
            gtln = curr.item.key
            curr = curr.right

        elif n < curr.item.key:
            curr = curr.left

    return gtln


def compare_BST(bst1, bst2):
    if len(bst1) != len(bst2):
        return False

    inorder1 = [key for key,val in bst1]
    inorder2 = [key for key,val in bst2]

    for i in range(min(len(inorder1), len(inorder2))):
        if inorder1[i] != inorder2[i]:
            return False
    return True


def is_BST(root):
    return is_BST_helper(root)


def is_BST_helper(root):
    if not root:
        return None, None, None

    lmin, lmax, lbst = is_BST_helper(root.left)
    rmin, rmax, rbst = is_BST_helper(root.right)

    if not (lbst and rbst):
        return None, None, False

    if lmax and lmax >= root.data:
        return None, None, False

    if rmin and rmin <= root.data:
        return None, None, False

    dmin = lmin or root.data
    dmax = rmax or root.data
    return (dmin, dmax, True)
