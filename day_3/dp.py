import io

def max_joltage_dp_optimized(bank_str, k):
    """
    Space-optimized DP: only keep track of current and previous row.
    """
    n = len(bank_str)
    print(f"n: {n}")
    
    # dp[j] = maximum number (as string) using exactly j digits so far
    prev = [""] * (k + 1)
    print(f"prev: {prev}")
    for i in range(n):
        print(f"i: {i}")
        digit = bank_str[i]
        print(f"digit: {digit}")
        curr = [""] * (k + 1)
        print(f"curr: {curr}")

        for j in range(k + 1):
            print(f"j: {j}")
            # Option 1: Skip current digit
            print(f"prev[j]: {prev[j]}")
            if prev[j] != "":
                curr[j] = prev[j]
            print(f"curr[j]: {curr[j]}")
            
            # Option 2: Take current digit
            if j > 0:
                print(f"prev[j - 1]: {prev[j - 1]}")
                if prev[j - 1] != "":
                    candidate = prev[j - 1] + digit
                    print(f"candidate: {candidate}")
                    if curr[j] == "" or candidate > curr[j]:
                        print(f"curr[j] before: {curr[j]}")
                        curr[j] = candidate
                        print(f"curr[j] after: {curr[j]}")
                elif j == 1:
                    print(f"j == 1")
                    # Start new sequence with this digit
                    if curr[j] == "" or digit > curr[j]:
                        print(f"curr[j] before: {curr[j]}")
                        curr[j] = digit
                        print(f"curr[j] after: {curr[j]}")
        
        prev = curr
        print(f"prev: {prev}")
    
    return int(prev[k])

# Read input
data = []
with io.open("day_3/simple_input.txt", "r") as file:
    for line in file:
        data.append(line.strip())

REQUIRED_BATTERY_SIZE = 12

total_joltage = 0
for bank in data[:1]:
    max_joltage = max_joltage_dp_optimized(bank, REQUIRED_BATTERY_SIZE)
    print(f"Max joltage: {max_joltage}")
    total_joltage += max_joltage

print(f"Total output joltage: {total_joltage}")