import csv
import os.path
import sys
from datetime import datetime

from matplotlib import pyplot as plt

from src.tests.DatasetType import DatasetType
from src.tests.Test import Test

data_structure_names = ['OL', 'BST', 'RBT']
dataset_types = ['rand', 'urand', 'ord', 'rev']
graphs_dir = os.path.join(os.path.dirname(__file__), 'graphs')


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


def read_data_structure(ds, algorithm, dataset_type):
    x = []
    data = [[], [], []]
    measurements_dir = os.path.join(os.path.dirname(__file__), 'measurements')
    csv_path = os.path.join(measurements_dir, ds + '\\' + algorithm + '_1000_' + dataset_type + '.csv')
    with open(csv_path, 'r') as file:
        lines = csv.reader(file, delimiter=',')
        next(lines, None)
        for row in lines:
            x.append(int(row[0]))
            data[0].append(int(row[1]))
            data[1].append(int(row[2]))
            data[2].append(int(row[3]))
    return x, data


def plot_by_data_structure(ds, algorithm, dataset_type):
    x, data = read_data_structure(ds, algorithm, dataset_type)
    fig, ax = plt.subplots()
    ax.plot(x, data[0], label='Worst case')
    ax.plot(x, data[1], label='Average case')
    ax.plot(x, data[2], label='Best case')
    ax.set_xlabel('n')
    ax.set_ylabel('time (ns)')
    if ds == 'RBT':
        ax.set_ylim(0, 5000)
    ax.set_title('{} {} {}'.format(ds, algorithm, dataset_type))
    ax.legend()
    ds_dir = os.path.join(graphs_dir, ds)
    filename = '{}_{}.png'.format(algorithm, dataset_type)
    plt.savefig(os.path.join(ds_dir, filename))
    plt.close()


def read_case(case, ds, algorithm, dataset_type):
    x = []
    data = []
    measurements_dir = os.path.join(os.path.dirname(__file__), 'measurements')
    csv_path = os.path.join(measurements_dir, ds + '\\' + algorithm + '_1000_' + dataset_type + '.csv')
    with open(csv_path, 'r') as file:
        lines = csv.DictReader(file, delimiter=',')
        for row in lines:
            x.append(int(row['n']))
            data.append(int(row[case]))
    return x, data


def plot_by_case(case, algorithm, dataset_type):
    data = {
        'OL': [],
        'BST': [],
        'RBT': []
    }
    for dsn in data_structure_names:
        x, ds_data = read_case(case, dsn, algorithm, dataset_type)
        data[dsn] = ds_data
    fig, ax = plt.subplots()
    ax.plot(x, data['OL'], label='Ordered list')
    ax.plot(x, data['BST'], label='Binary search tree')
    ax.plot(x, data['RBT'], label='Red-black tree')
    ax.set_xlabel('n')
    ax.set_ylabel('time (ns)')
    ax.set_title('{} {} case comparison {}'.format(algorithm, case, dataset_type))
    ax.legend()
    comp_dir = os.path.join(graphs_dir, 'comparisons')
    filename = '{}_{}_{}.png'.format(algorithm, case, dataset_type)
    plt.savefig(os.path.join(comp_dir, filename))
    plt.close()


if __name__ == '__main__':
    sys.setrecursionlimit(1100)
    run_all_tests()
    for dsn in data_structure_names:
        for dst in dataset_types:
            plot_by_data_structure(dsn, 'os_select', dst)
            plot_by_data_structure(dsn, 'os_rank', dst)

    for dst in dataset_types:
        plot_by_case('worst', 'os_select', dst)
        plot_by_case('worst', 'os_rank', dst)
        plot_by_case('average', 'os_select', dst)
        plot_by_case('average', 'os_rank', dst)
