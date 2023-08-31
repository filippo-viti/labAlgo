from src.data_structures.BinarySearchTreeNode import BinarySearchTreeNode
from src.data_structures.DataStructure import DataStructure


class BinarySearchTree(DataStructure):
    def __init__(self):
        self.root = None
        self.__counter = 0

    def insert(self, value):
        y = None
        x = self.root
        z = BinarySearchTreeNode(value)
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

    def os_select(self, i):
        self.__counter = 0
        return self.__os_select_tree_walk(self.root, i)

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

    def os_rank(self, k):
        self.__counter = 0
        return self.__os_rank_tree_walk(self.root, k)

    def __os_rank_tree_walk(self, x, k):
        if x is None:
            return None

        if x == k:
            self.__counter += 1
            return self.__counter

        left_index = self.__os_rank_tree_walk(x.left, k)
        if left_index is not None:
            return left_index
        if self.__counter == left_index:
            return x.value
        self.__counter += 1
        return self.__os_rank_tree_walk(x.right, k)
