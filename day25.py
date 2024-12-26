# Function to parse data from the input file
def parse_data(my_file) -> tuple:
    with open(my_file) as f:
        schematics = f.read().split('\n\n')
        keys = []
        locks = []
        for scheme in schematics:
            pins = [p.count('#') for p in zip(*scheme.split('\n'))]
            if scheme.startswith('#'):
                locks.append(pins)
            else:
                keys.append(pins)
        return locks, keys

# Function for Part 1
def part1(locks: list, keys: list) -> int:
    return sum(all(sum(pair) <= 7 for pair in zip(lock, key)) for lock in locks for key in keys)

# Main execution
if __name__ == "__main__":
    data = parse_data('input.txt')
    print('Part 1:', part1(*data))
