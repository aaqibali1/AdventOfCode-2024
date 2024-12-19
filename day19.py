def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    towel_patterns = lines[0].split(', ')
    designs = lines[2:]
    return towel_patterns, designs

def count_ways_to_make_design(design, towel_patterns):
    # Use a dictionary for memoization
    memo = {}

    def helper(remaining):
        if remaining == "":
            return 1
        if remaining in memo:
            return memo[remaining]

        ways = 0
        for pattern in towel_patterns:
            if remaining.startswith(pattern):
                ways += helper(remaining[len(pattern):])

        memo[remaining] = ways
        return ways

    return helper(design)

def part_one_possible_designs(towel_patterns, designs):
    def can_make_design(design):
        memo = {}

        def helper(remaining):
            if remaining == "":
                return True
            if remaining in memo:
                return memo[remaining]

            for pattern in towel_patterns:
                if remaining.startswith(pattern):
                    if helper(remaining[len(pattern):]):
                        memo[remaining] = True
                        return True

            memo[remaining] = False
            return False

        return helper(design)

    possible_count = 0
    for design in designs:
        if can_make_design(design):
            possible_count += 1

    return possible_count

def part_two_total_ways(towel_patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_make_design(design, towel_patterns)
    return total_ways

if __name__ == "__main__":
    input_file = "input.txt"
    towel_patterns, designs = parse_input(input_file)

    # Part One
    possible_designs = part_one_possible_designs(towel_patterns, designs)
    print(f"Number of possible designs: {possible_designs}")

    # Part Two
    total_ways = part_two_total_ways(towel_patterns, designs)
    print(f"Total number of ways to make designs: {total_ways}")
