from itertools import permutations
from numpy import array

# Initialize variables
codes = []

# Read the input file
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line.strip().endswith('A'):
            codes.append(line.strip())

# Position map
positions = {
    '7': array([0, 0]),
    '8': array([0, 1]),
    '9': array([0, 2]),
    '4': array([1, 0]),
    '5': array([1, 1]),
    '6': array([1, 2]),
    '1': array([2, 0]),
    '2': array([2, 1]),
    '3': array([2, 2]),
    '0': array([3, 1]),
    'A': array([3, 2]),
    '^': array([0, 1]),
    'a': array([0, 2]),
    '<': array([1, 0]),
    'v': array([1, 1]),
    '>': array([1, 2]),
}

# Directions map
directions = {
    '^': array([-1, 0]),
    'v': array([1, 0]),
    '<': array([0, -1]),
    '>': array([0, 1]),
}

# Memoization dictionary
ml_memos = {}

# Function to get moveset
def se_to_moveset(start, fin, avoid=array([0, 0])):
    delta = fin - start
    string = ''
    dx = delta[0]
    dy = delta[1]
    
    # Determine vertical movement
    if dx < 0:
        string += '^' * abs(dx)
    else:
        string += 'v' * dx
    
    # Determine horizontal movement
    if dy < 0:
        string += '<' * abs(dy)
    else:
        string += '>' * dy
    
    # Get all unique permutations
    rv = set()
    for s in permutations(string):
        path = [start]
        valid = True
        for move in s:
            next_pos = path[-1] + directions[move]
            if (next_pos == avoid).all():
                valid = False
                break
            path.append(next_pos)
        if valid:
            rv.add(''.join(s) + 'a')
    
    return ['a'] if not rv else list(rv)

# Function to calculate minimum length
def min_length(str, lim=2, depth=0):
    memo_key = (str, depth, lim)
    if memo_key in ml_memos:
        return ml_memos[memo_key]
    
    avoid = array([3, 0]) if depth == 0 else array([0, 0])
    cur = positions['A'] if depth == 0 else positions['a']
    
    length = 0
    for char in str:
        next_cur = positions[char]
        moveset = se_to_moveset(cur, next_cur, avoid)
        
        if depth == lim:
            length += len(moveset[0] if moveset else 'a')
        else:
            length += min(min_length(m, lim, depth + 1) for m in moveset)
        
        cur = next_cur
    
    ml_memos[memo_key] = length
    return length

# Complexity calculations
complexity_a = 0
complexity_b = 0
for code in codes:
    length_a = min_length(code)
    length_b = min_length(code, 25)
    numeric = int(code[:3])
    complexity_a += length_a * numeric
    complexity_b += length_b * numeric

# Output results
print(f"Part 1: {complexity_a}")
print(f"Part 2: {complexity_b}")
