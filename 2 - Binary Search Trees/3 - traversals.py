# Inorder traversal
# Traverse the left subtree recursively inorder.
# Traverse the current node.
# Traverse the right subtree recursively inorder.

class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])

    elif data is None:
        node = None

    else:
        node = TreeNode(data)
    return node


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = parse_tuple(tree_tuple)


def traverse_inorder(node):
    if node is None:
        return []
    return (traverse_inorder(node.left) + [node.key] + traverse_inorder(node.right))


print(traverse_inorder(tree))


# Preorder traversal
# Traverse the current node.
# Traverse the left subtree recursively preorder.
# Traverse the right subtree recursively preorder.

def traverse_preorder(node):
    if node is None:
        return []
    return ([node.key] + traverse_preorder(node.left) + traverse_preorder(node.right))


print(traverse_preorder(tree))


# Postorder traversal
# Traverse the leftmost node with no subtree.
# Traverse the left subtree rightmost node with no subtree.
# Recurseively.

def traverse_postorder(node):
    if node is None:
        return []
    return (traverse_postorder(node.left) + traverse_postorder(node.right) + [node.key])


print(traverse_postorder(tree))
