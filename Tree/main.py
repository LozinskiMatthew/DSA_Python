from numpy.lib.polynomial import roots


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return str(self.data)


def preorder_traversal(root, level = 0):
    if root is None:
        return
    print('    ' * level + root.data)
    preorder_traversal(root.left, level + 1)
    preorder_traversal(root.right, level + 1)


def inorder(root, level = 0):
    if root is None:
        return
    inorder(root.left, level + 1)
    print('    ' * level + root.data)
    inorder(root.right, level)


def postorder(root, level = 0):
    if root is None:
        return
    postorder(root.left, level + 1)
    postorder(root.right, level + 1)
    print('    ' * level + root.data)





if __name__ == "__main__":
    root = TreeNode("Shop")
    root.left = TreeNode("Electronics")
    root.right = TreeNode("Clothing")
    root.left.left = TreeNode("Phone")
    root.left.right = TreeNode("Laptop")
    root.right.left = TreeNode("Shirt")
    root.right.right = TreeNode("Skirt")

    print("Preorder Traversal")
    preorder_traversal(root)






