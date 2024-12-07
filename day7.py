from itertools import chain


def get_lines(filename):
    """Reads the input lines from the given file."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def clean_line(line):
    """Removes non-numeric characters like ':' from the line."""
    return ''.join(c if c.isdigit() or c.isspace() else ' ' for c in line)


def process_part1(lines):
    result = 0

    for line in lines:
        clean_data = clean_line(line)
        numbers = list(map(int, clean_data.split()))
        if not numbers:
            continue  # Skip empty or invalid lines

        target = numbers[0]
        rest = numbers[1:]

        possible_values = {rest[0]}
        for a in rest[1:]:
            possible_values = set(chain.from_iterable([(v + a, v * a) for v in possible_values]))

        if target in possible_values:
            result += target

    print(f"Part 1 Result: {result}")


def process_part2(lines):
    result = 0

    for line in lines:
        clean_data = clean_line(line)
        numbers = list(map(int, clean_data.split()))
        if not numbers:
            continue  # Skip empty or invalid lines

        target = numbers[0]
        rest = numbers[1:]

        possible_values = {rest[0]}
        for a in rest[1:]:
            new_values = set()
            for v in possible_values:
                new_values.update([v + a, v * a, int(f"{v}{a}")])
            possible_values = new_values

        if target in possible_values:
            result += target

    print(f"Part 2 Result: {result}")


if __name__ == "__main__":
    print("Day 7:")
    input_lines = get_lines("input.txt")
    process_part1(input_lines)
    process_part2(input_lines)
