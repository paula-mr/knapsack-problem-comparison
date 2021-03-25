from sort import sort_array

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