class BST:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.p = None

    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self, x, k):
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def os_select(self, i):
        pass

    def os_rank(self, x):
        pass
