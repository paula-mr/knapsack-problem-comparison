import sys
import os
from datetime import datetime


def main(argv):
    input_file, algorithm = get_startup_arguments(argv)
    weight, items = initialize_problem(input_file)
    
    start_time = datetime.now()
    if algorithm == 'bt':
        result = solve_knapsack_backtracking(weight, items)
    else:
        result = solve_knapsack_branch_and_bound(weight, items)
    end_time = datetime.now()

    diff = start_time - end_time

    print(result, diff.microseconds)


def solve_knapsack_backtracking(max_weight, items):
    items = sort_array(items)
    max_profit = recursive_backtracking(0, 0, max_weight, items)
    return max_profit

def recursive_backtracking(max_profit, current_profit, available_weight, items):
    if len(items) == 0:
        return current_profit

    item_profit, item_weight = items[0]
    new_profit = current_profit + item_profit
    new_available_weight = available_weight - item_weight

    if new_available_weight >= 0:
        result_adding_item = recursive_backtracking(max_profit, new_profit, new_available_weight, items[1:])
        if result_adding_item > max_profit:
            max_profit = result_adding_item
    
    result_not_adding_item = recursive_backtracking(max_profit, current_profit, available_weight, items[1:])
    if result_not_adding_item > max_profit:
        max_profit = result_not_adding_item
    
    return max_profit

    


def solve_knapsack_branch_and_bound(weight, items):
    items = sort_array(items)
    max_profit = 0
    queue = [(0,0)]

    return 0

def compute_ratio(item):
    return item[0]/item[1]

def sort_array(items):
    items.sort(reverse=True, key=compute_ratio)
    return items

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
        print("main.py <INPUT FILE> <ALGORITHM = bt | b&b>")
        os._exit(1)
    
    return input_file, algorithm

if __name__ == "__main__":
    main(sys.argv[1:])