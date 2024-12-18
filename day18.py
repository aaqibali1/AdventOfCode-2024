from collections import deque

def read_input(filename):
    """Reads the input file and returns a list of corrupted coordinates."""
    with open(filename, 'r') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def simulate_memory_space(corrupted_coords, grid_size, num_bytes):
    """Simulates the falling bytes and returns the grid state after num_bytes."""
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for i, (x, y) in enumerate(corrupted_coords):
        if i >= num_bytes:
            break
        grid[y][x] = '#'
    return grid

def find_shortest_path(grid, start, end):
    """Finds the shortest path from start to end in the grid using BFS."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] == '.':
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # No path found

def find_blocking_byte(corrupted_coords, grid_size):
    """Finds the first byte that prevents the exit from being reachable."""
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    for i, (x, y) in enumerate(corrupted_coords):
        grid[y][x] = '#'
        if find_shortest_path(grid, start, end) == -1:
            return x, y

    return None  # All bytes simulated, path never blocked

def main():
    # Input parameters
    filename = "input.txt"
    grid_size = 71  # For the full problem, adjust the grid size

    # Read input
    corrupted_coords = read_input(filename)

    # Part 1: Simulate memory space for first 1024 bytes and find shortest path
    num_bytes = 1024
    grid_after_bytes = simulate_memory_space(corrupted_coords, grid_size, num_bytes)
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    steps = find_shortest_path(grid_after_bytes, start, end)

    print(f"Minimum number of steps to reach the exit after {num_bytes} bytes: {steps}")

    # Part 2: Find the first blocking byte
    blocking_byte = find_blocking_byte(corrupted_coords, grid_size)

    if blocking_byte:
        print(f"First blocking byte: {blocking_byte[0]},{blocking_byte[1]}")
    else:
        print("No blocking byte found")

if __name__ == "__main__":
    main()
