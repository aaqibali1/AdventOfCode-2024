def count_xmas(grid):
    """Counts all occurrences of the word 'XMAS' in the grid."""
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (0, -1), # Horizontal left
        (-1, 0), # Vertical up
        (-1, -1),# Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]
    target = "XMAS"
    count = 0

    def check_word(r, c, dr, dc):
        for i in range(len(target)):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != target[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_word(r, c, dr, dc):
                    count += 1

    return count

def count_xmas_x_patterns(grid):
    """Counts all occurrences of the X-MAS pattern in the grid."""
    rows, cols = len(grid), len(grid[0])
    pattern_count = 0

    # Helper function to check if a diagonal forms a valid MAS
    def is_mas_diagonal(center_x, center_y):
        if (
            # Top-left to bottom-right diagonal: MAS or SAM
            (grid[center_x - 1][center_y - 1] == 'M' and
             grid[center_x][center_y] == 'A' and
             grid[center_x + 1][center_y + 1] == 'S') or
            (grid[center_x - 1][center_y - 1] == 'S' and
             grid[center_x][center_y] == 'A' and
             grid[center_x + 1][center_y + 1] == 'M')
        ) and (
            # Top-right to bottom-left diagonal: MAS or SAM
            (grid[center_x - 1][center_y + 1] == 'M' and
             grid[center_x][center_y] == 'A' and
             grid[center_x + 1][center_y - 1] == 'S') or
            (grid[center_x - 1][center_y + 1] == 'S' and
             grid[center_x][center_y] == 'A' and
             grid[center_x + 1][center_y - 1] == 'M')
        ):
            return True
        return False

    # Traverse the grid to count patterns
    for r in range(1, rows - 1):  # Avoid edges
        for c in range(1, cols - 1):  # Avoid edges
            if is_mas_diagonal(r, c):
                pattern_count += 1

    return pattern_count

def main():
    # Read input grid from input.txt
    with open("input.txt", "r") as file:
        grid = [line.strip() for line in file.readlines()]

    # Part 1: Count occurrences of 'XMAS'
    part_1_answer = count_xmas(grid)
    print(f"Part 1 Answer (Total occurrences of 'XMAS'): {part_1_answer}")

    # Part 2: Count occurrences of X-MAS patterns
    part_2_answer = count_xmas_x_patterns(grid)
    print(f"Part 2 Answer (Total occurrences of 'X-MAS'): {part_2_answer}")

if __name__ == "__main__":
    main()
