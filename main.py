import sys
import os
import time

from backtracking import solve_knapsack_backtracking
from branch_and_bound import solve_knapsack_branch_and_bound

def main(argv):
    input_file, algorithm = get_startup_arguments(argv)
    weight, items = initialize_problem(input_file)
    
    start_time = time.process_time()
    if algorithm == 'bt':
        result = solve_knapsack_backtracking(weight, items)
    else:
        result = solve_knapsack_branch_and_bound(weight, items)
    end_time = time.process_time()

    diff = end_time - start_time

    print(result, diff)


def initialize_problem(input_file):
    weight = None
    items = []
    with open(input_file, 'r') as file:
        lines = file.readlines()
        _, weight = lines[0].split(' ')
        lines = lines[1:]
        for line in lines:
            item_val, item_weight = line.split(' ')
            items += [(float(item_val.strip()), float(item_weight.strip()))]
    return float(weight.strip()), items
    

def get_startup_arguments(argv):
    input_file = None
    algorithm = None

    if len(argv) == 2:
        input_file = argv[0]
        algorithm = argv[1]
    else:
        print('Invalid arguments')
        print("main.py <INPUT FILE> <ALGORITHM = bt | bandb>")
        os._exit(1)
    
    return input_file, algorithm

if __name__ == "__main__":
    main(sys.argv[1:])