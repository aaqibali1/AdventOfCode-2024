def parse_input(file_name):
    with open(file_name, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads_and_scores(map_data):
    rows, cols = len(map_data), len(map_data[0])
    scores = {}

    def valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y, current_height):
        """Perform DFS to find reachable height 9 positions."""
        if not valid(x, y) or (x, y) in visited or map_data[x][y] != current_height:
            return 0
        visited.add((x, y))
        if current_height == 9:
            return 1

        score = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            score += dfs(x + dx, y + dy, current_height + 1)
        return score

    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] == 0:  # A trailhead
                visited = set()
                scores[(i, j)] = dfs(i, j, 0)

    return scores

def find_trailheads_and_ratings(map_data):
    rows, cols = len(map_data), len(map_data[0])
    ratings = {}

    def valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def count_paths(x, y, current_height):
        """Count distinct hiking trails starting at (x, y)."""
        if not valid(x, y) or map_data[x][y] != current_height:
            return 0
        if current_height == 9:
            return 1  # Reached height 9

        # Memoize results to avoid redundant calculations
        if (x, y, current_height) in memo:
            return memo[(x, y, current_height)]

        paths = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            paths += count_paths(x + dx, y + dy, current_height + 1)

        memo[(x, y, current_height)] = paths
        return paths

    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] == 0:  # A trailhead
                memo = {}
                ratings[(i, j)] = count_paths(i, j, 0)

    return ratings

def main():
    file_name = "input.txt"
    map_data = parse_input(file_name)

    # Part 1: Calculate scores of all trailheads
    trailhead_scores = find_trailheads_and_scores(map_data)
    total_score = sum(trailhead_scores.values())
    print("Part 1 - Sum of scores of all trailheads:", total_score)

    # Part 2: Calculate ratings of all trailheads
    trailhead_ratings = find_trailheads_and_ratings(map_data)
    total_rating = sum(trailhead_ratings.values())
    print("Part 2 - Sum of ratings of all trailheads:", total_rating)

if __name__ == "__main__":
    main()
