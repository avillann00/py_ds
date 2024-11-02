class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            return node(val)

        if root.val > val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def delete(self, root, val):
        if root is None:
            return

        if root.val < val:
            root.right = self.delete(root.right, val)
        elif root.val > val:
            root.left = self.delete(root.left, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                new = self.successor(root.right).val
                root.val = new.val
                root.right = self.delete(root.right, new.val)

        return root

    def successor(self, root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp

    def in_order(self, root):
        if root is None:
            return

        self.in_order(root.left)   
        print(f'[{root.val}] -> ', end='')
        self.in_order(root.right)

    def pre_order(self, root):
        if root is None:
            return
            
        print(f'[{root.val}] -> ', end='')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root):
        if root is None:
            return

        self.post_order(root.left)
        self.post_order(root.right)
        print(f'[{root.val}] -> ', end='')

tree = bst()
tree.root = tree.insert(tree.root, 4)
tree.root = tree.insert(tree.root, 2)
tree.root = tree.insert(tree.root, 10)
tree.root = tree.insert(tree.root, 19)
tree.root = tree.insert(tree.root, 1)
tree.root = tree.insert(tree.root, 3)
tree.root = tree.insert(tree.root, 12)
tree.pre_order(tree.root)
print()
tree.in_order(tree.root)
print()
tree.post_order(tree.root)
print()
tree.root = tree.delete(tree.root, 3)
tree.in_order(tree.root)
