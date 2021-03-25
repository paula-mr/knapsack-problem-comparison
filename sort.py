def compute_ratio(item):
    return item[0]/item[1]

def sort_array(items):
    items.sort(reverse=True, key=compute_ratio)
    return items