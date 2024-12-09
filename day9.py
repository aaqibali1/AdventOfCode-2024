# Function to print and copy output to clipboard
def pr(s):
    print(s)
    try:
        # Copy the result to clipboard if pyperclip is installed
        import pyperclip
        pyperclip.copy(s)
    except ImportError:
        pass  # Skip copying to clipboard if pyperclip is not available

# Set the recursion limit
def set_recursion_limit(limit):
    import sys
    sys.setrecursionlimit(limit)

set_recursion_limit(10**6)

# Input file name
infile = 'input.txt'

# Read data from the input file
with open(infile, 'r') as file:
    D = file.read().strip()

def solve(part2):
    A = []  # Will act as a deque
    SPACE = []  # Will act as a deque
    file_id = 0
    FINAL = []
    pos = 0
    
    # Process the input data
    for i, c in enumerate(D):
        if i % 2 == 0:
            if part2:
                A.append((pos, int(c), file_id))
            for _ in range(int(c)):
                FINAL.append(file_id)
                if not part2:
                    A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for _ in range(int(c)):
                FINAL.append(None)
                pos += 1
    
    # Rearrange files into spaces
    for (pos, sz, file_id) in reversed(A):
        for space_i in range(len(SPACE)):
            space_pos, space_sz = SPACE[space_i]
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos + i] == file_id, f'{FINAL[pos + i]=}'
                    FINAL[pos + i] = None
                    FINAL[space_pos + i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz - sz)
                break
    
    # Calculate the answer
    ans = 0
    for i, c in enumerate(FINAL):
        if c is not None:
            ans += i * c
    return ans

# Solve for part 1 and part 2
p1 = solve(False)
p2 = solve(True)

# Print the results
pr(p1)
pr(p2)
