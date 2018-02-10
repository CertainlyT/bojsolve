class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, left_data, right_data):
        if self.root is None:
            if data != ".":
                self.root = Node(data)
            if left_data != ".":
                self.root.left = Node(left_data)
            if right_data != ".":
                self.root.right = Node(right_data)
        else:
            self.search(self.root, data, left_data, right_data)

    def search(self, root, data, left_data, right_data):
        if root is None:
            return
        elif root.data == data:
            if left_data != ".":
                root.left = Node(left_data)
            if right_data != ".":
                root.right = Node(right_data)
        else:
            self.search(root.left, data, left_data, right_data)
            self.search(root.right, data, left_data, right_data)

    def preorder(self, root):
        print(root.data, end="")
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)

    def inorder(self, root):
        if root.left is not None:
            self.inorder(root.left)
        print(root.data, end="")
        if root.right is not None:
            self.inorder(root.right)

    def postorder(self, root):
        if root.left is not None:
            self.postorder(root.left)
        if root.right is not None:
            self.postorder(root.right)
        print(root.data, end="")


def main():
    n = int(input())
    t = Tree()
    for i in range(n):
        a, b, c = map(str, input().split())
        t.add(a, b, c)
    t.preorder(t.root)
    print()
    t.inorder(t.root)
    print()
    t.postorder(t.root)
    print()

main()