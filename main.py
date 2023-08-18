import random

from BST import BST

if __name__ == '__main__':
    tree = BST()
    for i in range(0, 10):
        tree.insert(random.randint(1, 30))
    tree.print_inorder(tree.root)
    print()
    print(tree.os_select(9).key)
