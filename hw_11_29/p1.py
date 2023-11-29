def bellNumber(n):
    """
    Calculate the nth Bell number using a dynamic programming approach.
    The result is modulo 10^9 + 7 to handle large numbers.
    
    Args:
    n (int): The number for which the Bell number is to be calculated.

    Returns:
    int: The nth Bell number modulo 10^9 + 7.
    """
    # Modulo value
    MOD = 10**9 + 7

    # Special case for n = 0
    if n == 0:
        return 1

    # Initialize a list to store Bell numbers, with an extra row for computation
    bell = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    # The first Bell number is 1
    bell[0][0] = 1

    # Fill the Bell triangle
    for i in range(1, n+1):
        # Explicitly set the first element of each row
        bell[i][0] = bell[i-1][i-1]

        # Fill the rest of the row
        for j in range(1, i+1):
            bell[i][j] = (bell[i-1][j-1] + bell[i][j-1]) % MOD

    # Return the last computed Bell number
    return bell[n][0]

# Test the function with the provided examples
test_cases = [0, 3, 5, 10, 1000]
results = [bellNumber(n) for n in test_cases]
print(results)
