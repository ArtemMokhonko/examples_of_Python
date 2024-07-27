class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Реалізація прямого обходу дерева:
def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Реалізація центрового обходу дерева:
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

# Реалізація зворотного обходу дерева:
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)
def sum_root(a, b):
    return a+b


# Створення дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left =Node(6)

print("Прямий обхід:")
preorder_traversal(root)

print("Центровий обхід:")
inorder_traversal(root)

print("Зворотний обхід:")
postorder_traversal(root)

print(sum_root(2,6))


