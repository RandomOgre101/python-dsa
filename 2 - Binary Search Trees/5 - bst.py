# A binary search tree or BST is a binary tree that satisfies the following conditions:
# The left subtree of any node only contains nodes with keys less than the node's key
# The right subtree of any node only contains nodes with keys greater than the node's key


class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node


def is_bst(node):
    if node is None:
        return True, float('inf'), float('-inf')

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(min_l, node.key, min_r)
    max_key = max(max_l, node.key, max_r)

    return is_bst_node, min_key, max_key


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_tuple(tree_tuple)
print(is_bst(tree))
