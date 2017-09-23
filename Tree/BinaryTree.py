class BinaryTree:

    class Node:

        def __init__(self, key, parent=None, left=None, right=None):
            self.key = key
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def getMiniNum(self):
        def _mininum(x):
            while x.left:
                x = x.left
            return x
        _mininum(self.root)

    def insert(self, key):
        newNode = self.Node(key)
        y = None
        x = self.root
        if not x:
            self.root = newNode
        else:
            while x:
                y = x
                if newNode.key > x.key:
                    x = x.right
                else:
                    x = x.left
            newNode.parent = y
            if y.key < newNode.key:
                y.right = newNode
            else:
                y.left = newNode

    def search(self, key):
        def _search(node, key):
            if node == None or key == node.key:
                return node
            if key < node.key:
                return self.search(node.left, key)
            else:
                return self.search(node.right, key)
        _search(self.root, key)

    def delete(self, z):
        def transplant(tree, u, v):
            if u.parent == None:
                tree.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            if v:
                v.parent = u.parent

        if z.left == None:
            transplant(self, z, z.rigth)
        elif z.right == None:
            transplant(self, z, z.left)
        else:
            y = self.mininum(z.right)
            if y.parent != z:
                transplant(self, y, y.right)
                y.right = z.right
                y.right.parent = y
            transplant(self, z, y)
            y.left = z.left
            y.left.parent = y