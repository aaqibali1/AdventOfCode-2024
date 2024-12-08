from collections import defaultdict
from itertools import combinations


def get_lines(filename):
    """Reads the input file and returns lines as a list of strings."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def parse_grid(lines):
    """Parses the grid into a dictionary of points and their corresponding values."""
    grid = {}
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char != '.':
                grid[(r, c)] = char
    return grid


def part1():
    """Solves part 1 of the problem."""
    inp = get_lines('input.txt')
    grid = parse_grid(inp)

    groups = defaultdict(list)
    for (r, c), char in grid.items():
        groups[char].append((r, c))

    ant = set()
    for k, v in groups.items():
        for (a, b) in combinations(v, 2):
            dr, dc = a[0] - b[0], a[1] - b[1]
            ant.add((a[0] + dr, a[1] + dc))
            ant.add((b[0] - dr, b[1] - dc))

    bounds = (len(inp), len(inp[0]))
    result = len([p for p in ant if 0 <= p[0] < bounds[0] and 0 <= p[1] < bounds[1]])
    print(result)


def part2():
    """Solves part 2 of the problem."""
    inp = get_lines('input.txt')
    grid = parse_grid(inp)

    groups = defaultdict(list)
    for (r, c), char in grid.items():
        groups[char].append((r, c))

    ant = set()
    bounds = (len(inp), len(inp[0]))
    for k, v in groups.items():
        for (a, b) in combinations(v, 2):
            dr, dc = b[0] - a[0], b[1] - a[1]
            
            # Extend in direction from a to b
            r, c = a[0], a[1]
            while 0 <= r < bounds[0] and 0 <= c < bounds[1]:
                ant.add((r, c))
                r += dr
                c += dc

            # Extend in direction from b to a
            r, c = b[0], b[1]
            while 0 <= r < bounds[0] and 0 <= c < bounds[1]:
                ant.add((r, c))
                r -= dr
                c -= dc

    print(len(ant))


if __name__ == "__main__":
    print("Day 8:")
    part1()
    part2()
