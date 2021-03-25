from sort import sort_array

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound


def solve_knapsack_branch_and_bound(weight, items):
    items = sort_array(items)
    n = len(items)
    max_profit = 0
    root = Node(-1, 0, 0, 0)
    queue = [root]

    while queue:
        node = queue[0]
        queue = queue[1:]

        if node.level == n-1:
            continue
        
        new_node_level = node.level+1
        new_node_profit = node.profit+items[node.level+1][0]
        new_node_weight = node.weight+items[node.level+1][1]
        new_node = Node(new_node_level, new_node_profit, new_node_weight, 0)
        
        # update max profit
        if new_node_weight <= weight and new_node_profit > max_profit:
            max_profit = new_node_profit
        
        # evaluate bound with the item
        new_node_bound = bound(new_node, n, weight, items)
        if new_node_bound > max_profit:
            new_node.bound = new_node_bound
            queue = [new_node] + queue
        
        # evaluate bound without the item    
        new_node = Node(new_node_level, node.profit, node.weight, 0)
        new_node_bound = bound(new_node, n, weight, items)
        if new_node_bound > max_profit:
            new_node.bound = new_node_bound
            queue = [new_node] + queue

    return max_profit

def bound(node, n, weight, items):
    if node.weight > weight:
        return 0

    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    while j < n and total_weight + items[j][1] <= weight:
        profit_bound += items[j][0]
        total_weight += items[j][1]
        j += 1
    
    if j < n:
        profit_bound += (weight - node.weight) * items[j][0]/items[j][1]
    
    return profit_bound
