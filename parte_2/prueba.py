def game_strategy(values):
    n = len(values)

    # Create a table to store the maximum sums we can achieve
    dp = [[0] * n for _ in range(n)]

    # Base case: when there's only one element to pick
    for i in range(n):
        dp[i][i] = values[i]

    # Fill the table for cases with more than one element
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1  # end index of the subarray
            # If you take values[i], the opponent can take either values[i+1] or values[j]
            take_i = values[i] + min(dp[i + 2][j] if i + 2 <= j else 0, dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            # If you take values[j], the opponent can take either values[i] or values[j-1]
            take_j = values[j] + min(dp[i + 1][j - 1] if i + 1 <= j - 1 else 0, dp[i][j - 2] if i <= j - 2 else 0)
            dp[i][j] = max(take_i, take_j)

    # Now we need to simulate the game to find the steps taken
    i, j = 0, n - 1
    your_steps = []
    opponent_steps = []

    # You always go first
    while i <= j:
        # Your turn
        if dp[i][j] == values[i] + min(dp[i + 2][j] if i + 2 <= j else 0, dp[i + 1][j - 1] if i + 1 <= j - 1 else 0):
            your_steps.append(values[i])
            i += 1
        else:
            your_steps.append(values[j])
            j -= 1

        # Opponent's turn
        if i <= j:  # Check if there are still elements to pick
            if dp[i][j] == values[j] + min(dp[i + 1][j - 1] if i + 1 <= j - 1 else 0, dp[i][j - 2] if i <= j - 2 else 0):
                opponent_steps.append(values[j])
                j -= 1
            else:
                opponent_steps.append(values[i])
                i += 1

    return your_steps, opponent_steps, sum(your_steps)

# Test with the specified array
values = [96, 594, 437, 674, 950]
your_steps, opponent_steps, your_total = game_strategy(values)
print("Your steps:", your_steps)
print("Opponent's steps:", opponent_steps)
print("Your total value:", your_total)