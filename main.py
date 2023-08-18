import random

from BST import BST

if __name__ == '__main__':
    tree = BST()
    for i in range(0, 10):
        tree.insert(random.randint(1, 30))
    tree.print_inorder(tree.root)
    k = tree.root.right
    index = tree.os_rank(k)
    print()
    print("Rank of node " + str(k.key) + " = " + str(index))
