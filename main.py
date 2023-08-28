from data_structures.RedBlackTree import RedBlackTree

if __name__ == '__main__':
    rbt = RedBlackTree()
    test_set = [2, 5, 6, 10, 15, 1, 4, 3, 9, 11]
    for i in range(10):
        rbt.insert(test_set[i])

    print(rbt.os_select(rbt.root, 1).key)
