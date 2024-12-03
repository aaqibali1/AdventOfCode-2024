import re

def calculate_conditional_mul_sum(file_name):
    # Read the content of the file
    with open(file_name, 'r') as file:
        content = file.read()
    
    # Regular expressions for instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'\bdo\(\)'
    dont_pattern = r'\bdon\'t\(\)'
    
    # Find all matches and their positions
    mul_matches = [(m.start(), int(m.group(1)), int(m.group(2))) for m in re.finditer(mul_pattern, content)]
    do_matches = [m.start() for m in re.finditer(do_pattern, content)]
    dont_matches = [m.start() for m in re.finditer(dont_pattern, content)]
    
    # Combine all instructions with their positions and sort them
    instructions = []
    instructions.extend([(pos, 'mul', x, y) for pos, x, y in mul_matches])
    instructions.extend([(pos, 'do') for pos in do_matches])
    instructions.extend([(pos, 'dont') for pos in dont_matches])
    instructions.sort()  # Sort by position in the file content
    
    # Process instructions and compute the sum
    enabled = True  # At the beginning, mul instructions are enabled
    total_sum = 0

    for instruction in instructions:
        if instruction[1] == 'mul':
            if enabled:
                total_sum += instruction[2] * instruction[3]
        elif instruction[1] == 'do':
            enabled = True
        elif instruction[1] == 'dont':
            enabled = False
    
    return total_sum

# File name as input
file_name = 'input3.txt'
result = calculate_conditional_mul_sum(file_name)
print(f"The sum of the results of the enabled multiplications is: {result}")
