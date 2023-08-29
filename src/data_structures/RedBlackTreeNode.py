from src.data_structures.BinarySearchTreeNode import BinarySearchTreeNode


class RedBlackTreeNode(BinarySearchTreeNode):
    def __init__(self, key, color):
        super().__init__(key)
        self.color = color  # False = Black, True = Red
        self.size = 1
