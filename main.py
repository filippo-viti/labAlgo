import csv
import os.path
import sys
from datetime import datetime

from matplotlib import pyplot as plt

from src.tests.DatasetType import DatasetType
from src.tests.Test import Test

plot_only = False
data_structure_names = ['OL', 'BST', 'RBT']


def run_all_tests():
    tests = []
    for ds in data_structure_names:
        tests.append(Test(ds, DatasetType.RANDOM))
        tests.append(Test(ds, DatasetType.UNIQUE_RANDOM))
        tests.append(Test(ds, DatasetType.ORDERED))
        tests.append(Test(ds, DatasetType.REVERSED))
    start = datetime.now()
    for test in tests:
        test.run()
    end = datetime.now()
    elapsed_time = (end - start).total_seconds()
    print("Total time = " + str(elapsed_time) + " s")


def read_data(ds):
    x = []
    data = [[], [], []]
    measurements_dir = os.path.join(os.path.dirname(__file__), 'measurements')
    csv_path = os.path.join(measurements_dir, ds + '\\os_select_1000_urand.csv')
    with open(csv_path, 'r') as file:
        lines = csv.reader(file, delimiter=',')
        next(lines, None)
        for row in lines:
            x.append(int(row[0]))
            data[0].append(int(row[1]))
            data[1].append(int(row[2]))
            data[2].append(int(row[3]))
    return x, data


def plot(ds):
    graphs_dir = os.path.join(os.path.dirname(__file__), 'graphs')
    x, data = read_data(ds)
    fig, ax = plt.subplots()
    ax.plot(x, data[0], label='Worst case')
    ax.plot(x, data[1], label='Average case')
    ax.plot(x, data[2], label='Best case')
    ax.set_xlabel('n')
    ax.set_ylabel('time (ns)')
    if ds == 'RBT':
        ax.set_ylim(0, 5000)
    ax.set_title('OS_SELECT')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    sys.setrecursionlimit(1100)
    if not plot_only:
        run_all_tests()

    for ds in data_structure_names:
        plot(ds)
