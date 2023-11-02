# QUESTION 2: Implement a binary tree using Python, and show its usage with some examples.


class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# With Tuple:
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


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


tree2 = parse_tuple(tree_tuple)


def tree_to_tuple(node):
    if node is None:
        return None

    if node.left is None and node.right is None:
        return node.key

    left_tuple = tree_to_tuple(node.left) if node.left else None
    right_tuple = tree_to_tuple(node.right) if node.right else None

    return (left_tuple, node.key, right_tuple)


tp = tree_to_tuple(tree2)
print(tp)
