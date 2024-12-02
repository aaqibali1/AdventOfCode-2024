def is_safe(level):
    """
    Check if the given level is safe based on the criteria:
    - It is either strictly increasing or strictly decreasing.
    - The distance between adjacent elements is between 1 and 3 inclusive.
    """
    is_only_increasing = all(level[i] < level[i + 1] for i in range(len(level) - 1))
    is_only_decreasing = all(level[i] > level[i + 1] for i in range(len(level) - 1))
    is_distance_ok = all(1 <= abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1))
    
    return (is_only_increasing ^ is_only_decreasing) and is_distance_ok


def is_safe_with_removal(level):
    """
    Check if the given level is safe or can be made safe by removing one element.
    """
    if is_safe(level):
        return True

    # Try removing each element and check if the modified list is safe
    for i in range(len(level)):
        modified_level = level[:i] + level[i+1:]
        if is_safe(modified_level):
            return True

    return False


def main():
    # Read input from input.txt
    with open("input.txt", "r") as file:
        input_data = file.read().strip().splitlines()
    
    reports = [
        list(map(int, line.split())) for line in input_data
    ]
    
    part1_answer = sum(1 for report in reports if is_safe(report))
    part2_answer = sum(1 for report in reports if is_safe_with_removal(report))

    print(part1_answer)
    print(part2_answer)


if __name__ == "__main__":
    main()
