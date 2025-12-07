import io

data = []
with io.open("day_7/input.txt", "r") as file:
    for line in file:
        # Turn line to list
        line_list = list(line.strip())
        data.append(line_list)

start_col = None
for row_idx, row in enumerate(data):
    for col_idx, char in enumerate(row):
        if char == 'S':
            start_col = col_idx

dp = [dict() for _ in range(len(data))]
dp[0][start_col] = 1  # One timeline starts at S

for row_idx in range(1, len(data)):
    dp[row_idx] = {}
    
    # Process all positions from previous row that have timelines
    for col, count in dp[row_idx - 1].items():
        if data[row_idx][col] == '.':
            # Timelines continue straight to the same column
            dp[row_idx][col] = dp[row_idx].get(col, 0) + count
        elif data[row_idx][col] == '^':
            # Timelines split, should take into account number of timelines that can reach the current column
            # If timelines reach the same column, they should be added together
            dp[row_idx][col - 1] = dp[row_idx].get(col - 1, 0) + count
            dp[row_idx][col + 1] = dp[row_idx].get(col + 1, 0) + count

# print(dp)
# print(dp[-1].values())
answer = sum(dp[-1].values())

print(f"Answer: {answer}")