from functools import cache

def intlist(line):
    """Convert a line of space-separated numbers into a list of integers."""
    return list(map(int, line.split()))

def read_input(filename):
    """Read the input file and return the list of initial stones."""
    with open(filename, 'r') as file:
        return intlist(file.readline().strip())

@cache
def how_many_eventually(x, iters):
    """Compute how many stones will result from a single stone after a given number of iterations."""
    if iters == 0:
        return 1

    if x == 0:
        return how_many_eventually(1, iters - 1)

    n = len(str(x))

    if n % 2 == 0:
        a = int(str(x)[:n // 2])
        b = int(str(x)[n // 2:])
        return (
            how_many_eventually(a, iters - 1) +
            how_many_eventually(b, iters - 1)
        )

    return how_many_eventually(x * 2024, iters - 1)

def compute_total_stones(filename, iters):
    """Compute the total number of stones after a given number of iterations."""
    stones = read_input(filename)
    return sum(how_many_eventually(x, iters) for x in stones)

if __name__ == "__main__":
    input_file = "input.txt"

    # Part One
    iterations_part_one = 25
    result_part_one = compute_total_stones(input_file, iterations_part_one)
    print(f"Total number of stones after {iterations_part_one} iterations: {result_part_one}")

    # Part Two
    iterations_part_two = 75
    result_part_two = compute_total_stones(input_file, iterations_part_two)
    print(f"Total number of stones after {iterations_part_two} iterations: {result_part_two}")
