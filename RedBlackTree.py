class RedBlackTree:
    class Node:
        def __init__(self, key, color):
            self.key = key
            self.left = None
            self.right = None
            self.p = None
            self.color = color  # False = Black, True = Red
            self.size = 0

    def __init__(self):
        self.root = None
        self.NIL = self.Node(None, False)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def insert(self, z):
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            x.size += 1  # size increment
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = True
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p.color:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color:
                    z.p.color = False
                    y.color = False
                    z.p.p.color = True
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = False
                    z.p.p.color = True
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color:
                    z.p.color = False
                    y.color = False
                    z.p.p.color = True
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = False
                    z.p.p.color = True
                    self.left_rotate(z.p.p)
        self.root.color = False

    def os_select(self, x, i):
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return self.os_select(x.left, i)
        else:
            return self.os_select(x.right, i - r)

    def os_rank(self, x):
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y == y.p.right:
                r = r + y.p.left.size + 1
            y = y.p
        return r
