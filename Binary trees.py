class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def tree():
    data = input("Enter node value (or 'None' for no node): ")
    if data.lower() == 'none':
        return None
    node = Node(data)
    print(f"Enter left child of {data}")
    node.left = tree()
    print(f"Enter right child of {data}")
    node.right = tree()
    return node
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')
print("Build the binary tree:")
root = tree()

print("\nPreorder Traversal:")
preorder(root)

print("\nInorder Traversal:")
inorder(root)

print("\nPostorder Traversal:")
postorder(root)
