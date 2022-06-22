class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None
            self.left_count = 0
            self.right_count = 0

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None
            self.left_count = None
            self.right_count = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.find(key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def find(self, key):
        curr = self.root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.find(key)
        if (node is None):
            self.insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
                parent.left_count += 1
            else:
                curr = self.root.right
                parent.right_count += 1
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                    parent.left_count += 1
                else:
                    curr = curr.right
                    parent.right_count += 1
            if (key < parent.item.key):
                parent.left = new_node

            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1


    # raises exception if key not in tree
    def __delitem__(self, key):
        node = self.find(key)
        if (node is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.delete_node(node)

    # assumes key is in tree + returns value assosiated
    def delete_node(self, node_to_delete):
        item = node_to_delete.item
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                    self.root.left_count = 0
                else:
                    self.root = self.root.right
                    self.root.left_count = 0
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                node_to_delete.left_count -= 1
                self.delete_node(max_of_left)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent

                if (node_to_delete is parent.left):
                    parent.left = child
                    parent.left_count -= 1
                else:
                    parent.right = child
                    parent.right_count -= 1

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                node_to_delete.left_count -= 1
                self.delete_node(max_of_left)

        return item

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)


    def __iter__(self):
        for node in self.inorder():
            yield node.item.key


    def get_ith_smallest(self, i):
        if i > self.root.left_count + self.root.right_count + 1:
            raise IndexError("i is out of range")
        return self.get_ith_smallest_helper(i, self.root)


    def get_ith_smallest_helper(self, i, root):
        if i == root.left_count + 1:
            return root.item.key
        elif i <= root.left_count:
            return self.get_ith_smallest_helper(i, root.left)
        else:
            return self.get_ith_smallest_helper(i - root.left_count - 1, root.right)



bst = BinarySearchTreeMap()
bst[7] = None
bst[5] = None
bst[1] = None
bst[14] = None
bst[10] = None
bst[3] = None
bst[9] = None
bst[13] = None
# print(bst.get_ith_smallest(3))
# print(bst.get_ith_smallest(6))
# bst.__delitem__(14)
# bst.__delitem__(5)
# print(bst.get_ith_smallest(3))
# print(bst.get_ith_smallest(6))

