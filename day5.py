def read_input(file_name):
    """Read input rules and updates from the file."""
    with open(file_name) as f:
        rules, updates = f.read().strip().split('\n\n')
        rules = [tuple(map(int, r.split('|'))) for r in rules.splitlines()]
        updates = [list(map(int, u.split(','))) for u in updates.splitlines()]
    return rules, updates

def is_ordered(update, rules):
    """Check if the update respects the rules."""
    positions = {page: idx for idx, page in enumerate(update)}
    return all(positions.get(x, -1) < positions.get(y, -1) for x, y in rules if x in positions and y in positions)

def reorder_update(update, rules):
    """Reorder the update based on the rules."""
    graph = {page: [] for page in update}
    indegree = {page: 0 for page in update}
    
    # Build a directed graph and indegree map
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            indegree[y] += 1
    
    # Perform topological sorting
    queue = [page for page in update if indegree[page] == 0]
    sorted_order = []
    
    while queue:
        current = queue.pop(0)
        sorted_order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def main():
    rules, updates = read_input('input.txt')
    correct_middle_sum = 0
    incorrect_middle_sum = 0

    for update in updates:
        if is_ordered(update, rules):
            # Part One: Add middle page for correctly ordered updates
            correct_middle_sum += update[len(update) // 2]
        else:
            # Part Two: Reorder and add middle page for incorrect updates
            reordered = reorder_update(update, rules)
            incorrect_middle_sum += reordered[len(reordered) // 2]

    print("Sum of middle pages for correctly ordered updates:", correct_middle_sum)
    print("Sum of middle pages for corrected updates:", incorrect_middle_sum)

if __name__ == "__main__":
    main()
