import random

from data_structures.BinarySearchTree import BinarySearchTree
from data_structures.OrderedList import OrderedList
from data_structures.RedBlackTree import RedBlackTree
from tests.DatasetType import DatasetType


class Generator:
    structures = {
        "OL": OrderedList,
        "BST": BinarySearchTree,
        "RBT": RedBlackTree,
    }

    @classmethod
    def get(cls, data_structure, size, dataset_type):
        ds = cls.structures[data_structure]()
        match dataset_type:
            case DatasetType.RANDOM:
                for i in range(size):
                    ds.insert(random.randint(1, size))
            case DatasetType.UNIQUE_RANDOM:
                dataset = list(range(1, size + 1))
                random.shuffle(dataset)
                for i in range(size):
                    ds.insert(dataset[i])
            case DatasetType.ORDERED:
                for i in range(1, size + 1):
                    ds.insert(i)
            case DatasetType.REVERSED:
                for i in range(size, 0, -1):
                    ds.insert(i)
        return ds
