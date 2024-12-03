import re

def calculate_mul_sum(file_name):
    # Read the content of the file
    with open(file_name, 'r') as file:
        content = file.read()
    
    # Regular expression to find valid mul(X,Y) instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches
    matches = re.findall(pattern, content)
    
    # Calculate the sum of products
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

# File name as input
file_name = 'input3.txt'
result = calculate_mul_sum(file_name)
print(f"The sum of the results of the multiplications is: {result}")
