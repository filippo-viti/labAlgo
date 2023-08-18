class BST:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.p = None

    def __init__(self):
        self.root = None
        self.__counter = 0

    def insert(self, z):
        y = None
        x = self.root
        z = self.Node(z)
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

    def print_inorder(self, x):
        if x:
            self.print_inorder(x.left)
            print(x.key, end=" ")
            self.print_inorder(x.right)

    def os_select(self, i):
        self.__counter = 0
        return self.__os_select_tree_walk(self.root, i)
        pass

    def __os_select_tree_walk(self, x, i):
        if x is None:
            return None
        if self.__counter <= i:
            left_node = self.__os_select_tree_walk(x.left, i)
            if left_node is not None:
                return left_node
            if self.__counter == i:
                return x
            self.__counter += 1
            return self.__os_select_tree_walk(x.right, i)

    def os_rank(self, x):
        pass
