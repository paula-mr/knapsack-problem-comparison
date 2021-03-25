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


def bound(node, n, weight, items):
    level, profit, current_weight = node
    if current_weight > weight:
        return 0

    profit_bound = profit
    j = level + 1
    total_weight = current_weight

    while j < n and total_weight + items[j][1] <= weight:
        profit_bound += items[j][0]
        total_weight += items[j][1]
        j += 1
    
    print('a', total_weight, profit_bound)
    if j < n:
        profit_bound += (weight - current_weight) * items[j][0]/items[j][1]
    
    return profit_bound


def solve_knapsack_branch_and_bound(weight, items):
    items = sort_array(items)
    n = len(items)
    max_profit = 0
    root = (-1, 0, 0) # level, profit, weight
    queue = [root]

    while queue:
        node = queue[0]
        queue = queue[1:]

        node_level = node[0]
        node_profit = node[1]
        node_weight = node[2]

        if node_level == n-1:
            continue
        
        new_node_level = node_level+1
        new_node_profit = node_profit+items[node_level+1][0]
        new_node_weight = node_weight+items[node_level+1][1]

        # taking the item
        if new_node_weight <= weight and new_node_profit > max_profit:
            max_profit = new_node_profit
        new_node_bound = bound((new_node_level, new_node_profit, new_node_weight), n, weight, items)

        print (new_node_bound, max_profit)
        if new_node_bound > max_profit:
            queue = [(new_node_level, new_node_profit, new_node_weight)] + queue
        
        # without taking the item        
        new_node_weight = node_weight
        new_node_profit = node_profit
        new_node_bound = bound((new_node_level, new_node_profit, new_node_weight), n, weight, items)

        print (new_node_bound, max_profit)
        if new_node_bound > max_profit:
            queue = [(new_node_level, new_node_profit, new_node_weight)] + queue

    return max_profit

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
        print("main.py <INPUT FILE> <ALGORITHM = bt | bandb>")
        os._exit(1)
    
    return input_file, algorithm

if __name__ == "__main__":
    main(sys.argv[1:])