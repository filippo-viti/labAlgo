from datetime import datetime

from src.tests.DatasetType import DatasetType
from src.tests.Test import Test

plot_only = False


def run_all_tests():
    OL_test = Test('OL', DatasetType.RANDOM)
    BST_test = Test('BST', DatasetType.RANDOM)
    RBT_test = Test('RBT', DatasetType.RANDOM)
    start = datetime.now()
    OL_test.run()
    BST_test.run()
    RBT_test.run()
    end = datetime.now()
    elapsed_time = (end - start).total_seconds()
    print("Total time = " + str(elapsed_time) + " s")


def plot():
    pass


if __name__ == '__main__':
    if not plot_only:
        run_all_tests()
    plot()
