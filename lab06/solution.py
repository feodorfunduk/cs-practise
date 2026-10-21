def count_items(values: list) -> dict:
    counts = {}
    for item in values:
        counts['item'] = counts.get(item, 0) + 1
    return counts

def unique_sorted(values: list) -> list:
    return sorted(set(values))



