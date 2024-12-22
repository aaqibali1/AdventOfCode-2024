# Define the function to compute the next secret number in the sequence
def generate_next_secret(secret_number):
    secret_number ^= (secret_number * 64) % 16777216
    secret_number %= 16777216
    secret_number ^= (secret_number // 32) % 16777216
    secret_number %= 16777216
    secret_number ^= (secret_number * 2048) % 16777216
    secret_number %= 16777216
    return secret_number

# Define the function to compute the 2000th secret number for a given initial secret
def calculate_2000th_secret(initial_secret):
    MODULO = 16777216  # Modulo value for pruning
    secret = initial_secret

    # Generate the sequence up to the 2000th secret number
    for _ in range(2000):
        secret = (secret ^ (secret * 64)) % MODULO
        secret = (secret ^ (secret // 32)) % MODULO
        secret = (secret ^ (secret * 2048)) % MODULO

    return secret

# Define the function to generate the price sequence
def get_price_sequence(initial_secret):
    # Generate all prices at once
    prices = []
    secret = initial_secret
    for _ in range(2001):  # We need 2001 to get 2000 changes
        prices.append(secret % 10)
        secret = generate_next_secret(secret)
    return prices

# Define the function to find sequences in the price changes
def find_sequences(prices):
    # Create a dictionary to store where each sequence appears and its corresponding price
    sequences = {}
    changes = []

    # Calculate all changes
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i-1])

    # For each position, record the 4-change sequence that starts there
    for i in range(len(changes) - 3):
        seq = tuple(changes[i:i+4])  # Convert to tuple so it can be used as dict key
        if seq not in sequences:  # Only keep the first occurrence
            sequences[seq] = prices[i+4]

    return sequences

# Main function to process the input file and calculate the result
def monkey_market_sum(filename="input.txt"):
    with open(filename, "r") as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    # Calculate the sum of the 2000th secret numbers
    result_sum = sum(calculate_2000th_secret(secret) for secret in initial_secrets)

    return result_sum

# Main function to process sequences and find the best one
def main():
    with open("input.txt", "r") as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    # Pre-calculate all sequences for each buyer
    buyer_sequences = []
    for secret in initial_secrets:
        prices = get_price_sequence(secret)
        sequences = find_sequences(prices)
        buyer_sequences.append(sequences)

    # Find the sequence that appears in most buyers with highest total
    best_total = 0
    best_sequence = None

    # Get all unique sequences that appear in any buyer's data
    all_sequences = set()
    for sequences in buyer_sequences:
        all_sequences.update(sequences.keys())

    # Check each sequence that actually appears in the data
    for seq in all_sequences:
        total = sum(sequences.get(seq, 0) for sequences in buyer_sequences)
        if total > best_total:
            best_total = total
            best_sequence = seq

    print(f"Best sequence: {list(best_sequence)}")
    print(f"Maximum bananas: {best_total}")

    # Calculate the sum of the 2000th secret numbers
    result_sum = monkey_market_sum("input.txt")
    print(f"Sum of the 2000th secret numbers: {result_sum}")

if __name__ == "__main__":
    main()
