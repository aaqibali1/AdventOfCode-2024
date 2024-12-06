def part1():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    w = len(lines[0].strip())
    h = len(lines)
    
    # Create the matrix from input
    mat = [list(line.strip()) for line in lines]

    pos = (0, 0)

    # Find initial position of '^'
    for y in range(h):
        for x in range(w):
            if mat[y][x] == '^':
                pos = (x, y)
                break

    states = set()
    visited = [[False] * w for _ in range(h)]
    visited[pos[1]][pos[0]] = True

    dir = (0, -1)

    def in_bounds(x, y):
        return 0 <= x < w and 0 <= y < h

    while (pos, dir) not in states:
        visited[pos[1]][pos[0]] = True
        states.add((pos, dir))

        # Check boundary before accessing
        new_x, new_y = pos[0] + dir[0], pos[1] + dir[1]
        while in_bounds(new_x, new_y) and mat[new_y][new_x] == '#':
            dir = (-dir[1], dir[0])
            new_x, new_y = pos[0] + dir[0], pos[1] + dir[1]

        if not in_bounds(new_x, new_y) or mat[new_y][new_x] == ' ':
            break

        pos = (new_x, new_y)

    # Count the number of visited positions
    count = sum(sum(row) for row in visited)
    return count


def part2():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    w = len(lines[0].strip())
    h = len(lines)
    
    # Create the matrix from input
    mat = [list(line.strip()) for line in lines]

    startpos = None

    # Find initial position of '^'
    for y in range(h):
        for x in range(w):
            if mat[y][x] == '^':
                startpos = (x, y)
                break
        if startpos:
            break

    c = 0
    states = set()

    def in_bounds(x, y):
        return 0 <= x < w and 0 <= y < h

    for y in range(h):
        for x in range(w):
            if mat[y][x] == '#':
                continue

            mat[y][x] = '#'
            states.clear()

            dir = (0, -1)
            pos = startpos
            isloop = True

            while (pos, dir) not in states:
                states.add((pos, dir))

                # Check boundary before accessing
                new_x, new_y = pos[0] + dir[0], pos[1] + dir[1]
                while in_bounds(new_x, new_y) and mat[new_y][new_x] == '#':
                    dir = (-dir[1], dir[0])
                    new_x, new_y = pos[0] + dir[0], pos[1] + dir[1]

                if not in_bounds(new_x, new_y) or mat[new_y][new_x] == ' ':
                    isloop = False
                    break

                pos = (new_x, new_y)

            if isloop:
                c += 1

            mat[y][x] = '.'

    return c


# Running both parts
print("Part 1:", part1())
print("Part 2:", part2())
