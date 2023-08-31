import csv
import gc
import os.path
import time

import yaml

from src.tests.DatasetType import DatasetType
from src.tests.Generator import Generator


class Test:
    def __init__(self, data_structure, dataset_type):
        self.data_structure = data_structure
        self.dataset_type = dataset_type

    def run(self):
        conf_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        with open(conf_path, 'r') as file:
            params = yaml.safe_load(file)
        times = {
            'os_select': [],
            'os_rank': []
        }
        # TODO introduce step parameter
        for n in range(1, params['max_size'] + 1):
            print("Running {} test: {}/{}".format(self.data_structure, n, params['max_size']), end='\r')
            ds = Generator.get(self.data_structure, n, self.dataset_type)

            cases = {
                'worst': n,
                'average': n // 2 + 1,
                'best': 1,
            }

            os_select_row = [n]
            os_rank_row = [n]
            for case, i in cases.items():
                results = self.__run_repetitions(ds, i, params['repetitions'])
                os_select_row.append(results['os_select'])
                os_rank_row.append(results['os_rank'])
            times['os_select'].append(os_select_row)
            times['os_rank'].append(os_rank_row)
        print()
        self.__write_results(times)


    def __run_repetitions(self, ds, case_i, rep):
        current_n_times = {
            'os_select': [],
            'os_rank': []
        }
        gc.disable()
        for i in range(rep):
            start = time.perf_counter_ns()
            x = ds.os_select(case_i)
            end = time.perf_counter_ns()
            current_n_times['os_select'].append(end - start)

            start = time.perf_counter_ns()
            ds.os_rank(x)
            end = time.perf_counter_ns()
            current_n_times['os_rank'].append(end - start)
        min_times = {
            'os_select': min(current_n_times['os_select']),
            'os_rank': min(current_n_times['os_rank']),
        }
        gc.enable()
        return min_times

    def __write_results(self, times):
        header = ['n', 'worst', 'average', 'best']
        ds_dir_path = os.path.join(os.path.dirname(__file__), '..\\..\\measurements\\' + self.data_structure)

        match self.dataset_type:
            case DatasetType.RANDOM:
                ds_type_string = 'rand'
            case DatasetType.UNIQUE_RANDOM:
                ds_type_string = 'urand'
            case DatasetType.ORDERED:
                ds_type_string = 'ord'
            case DatasetType.REVERSED:
                ds_type_string = 'rev'
        os_select_path = os.path.join(ds_dir_path,
                                      'os_select_{}_{}.csv'.format(len(times['os_select']), ds_type_string))
        with open(os_select_path, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for t in times['os_select']:
                writer.writerow(t)

        os_rank_path = os.path.join(ds_dir_path, 'os_rank_{}_{}.csv'.format(len(times['os_rank']), ds_type_string))
        with open(os_rank_path, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for t in times['os_rank']:
                writer.writerow(t)
