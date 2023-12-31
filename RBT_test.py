import gc
import random
import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from RedBlackTree import RedBlackTree

MAX_SAMPLE_SIZE = 1000


def fill(t, n):
    for i in range(n):
        t.insert(random.randint(1, 5000))


def os_select_test(l, i):
    start = time.perf_counter_ns()
    x = l.os_select(l.root, i)
    end = time.perf_counter_ns()
    elapsed_time = end - start
    return elapsed_time, x


def os_rank_test(l, x):
    start = time.perf_counter_ns()
    l.os_rank(x)
    end = time.perf_counter_ns()
    elapsed_time = end - start
    return elapsed_time


def plot_os_select(data):
    fig, ax = plt.subplots()
    x = np.linspace(1, MAX_SAMPLE_SIZE, MAX_SAMPLE_SIZE)
    ax.plot(x, data[0], label='Worst case')
    ax.plot(x, data[1], label='Average case')
    ax.plot(x, data[2], label='Best case')
    ax.set_xlabel('n')
    ax.set_ylabel('time')
    ax.set_title("OS_SELECT")
    ax.legend()
    plt.savefig('graphs/RBT/os_select.png')


def plot_os_rank(data):
    fig, ax = plt.subplots()
    x = np.linspace(1, MAX_SAMPLE_SIZE, MAX_SAMPLE_SIZE)
    ax.plot(x, data[0], label='Worst case')
    ax.plot(x, data[1], label='Average case')
    ax.plot(x, data[2], label='Best case')
    ax.set_xlabel('n')
    ax.set_ylabel('time')
    ax.set_title("OS_RANK")
    ax.legend()
    plt.savefig('graphs/RBT/os_rank.png')


if __name__ == '__main__':
    start = datetime.now()
    os_select_times = [[], [], []]
    os_rank_times = [[], [], []]

    for i in range(MAX_SAMPLE_SIZE):
        n = i + 1
        tree = RedBlackTree()
        fill(tree, n)

        gc.disable()
        # os_select tests
        os_select_worst_time, os_select_worst_result = os_select_test(tree, n)
        os_select_avg_time, os_select_avg_result = os_select_test(tree, (n // 2) + 1)
        os_select_best_time, os_select_best_result = os_select_test(tree, 1)

        os_select_times[0].append(os_select_worst_time)
        os_select_times[1].append(os_select_avg_time)
        os_select_times[2].append(os_select_best_time)

        # os_rank tests
        os_rank_times[0].append(os_rank_test(tree, os_select_worst_result))
        os_rank_times[1].append(os_rank_test(tree, os_select_avg_result))
        os_rank_times[2].append(os_rank_test(tree, os_select_best_result))

        del tree
        gc.enable()

    plot_os_select(os_select_times)
    plot_os_rank(os_rank_times)

    end = datetime.now()
    elapsed_time = (end - start).total_seconds()

    print("Total time = " + str(elapsed_time) + " s")
