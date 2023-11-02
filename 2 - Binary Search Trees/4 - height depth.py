# Tree Height: Length of longest path from its root node to a leaf
# 1 + max(height of left subtree | height of right subtree)

# Number of nodes: 1 + size(left subtree) + size(right_subtree)

class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_inorder(self):
        if self is None:
            return []
        return (TreeNode.traverse_inorder(self.left) + [self.key] + TreeNode.traverse_inorder(self.right))

    def traverse_preorder(self):
        if self is None:
            return []
        return ([self.key] + TreeNode.traverse_preorder(self.left) + TreeNode.traverse_preorder(self.right))

    def traverse_postorder(self):
        if self is None:
            return []
        return (TreeNode.traverse_postorder(self.left) + TreeNode.traverse_postorder(self.right) + [self.key])

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
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


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_tuple(tree_tuple)
print(tree.height())
