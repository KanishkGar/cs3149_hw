def catalan(n):
    """
    Calculate the nth Catalan number using dynamic programming.
    The result is modulo 10^9 + 7 to handle large numbers.

    Args:
    n (int): The number for which the Catalan number is to be calculated.

    Returns:
    int: The nth Catalan number modulo 10^9 + 7.
    """
    # Modulo value
    MOD = 10**9 + 7

    # Base case
    if n <= 1:
        return 1

    # Table to store results of subproblems
    catalan_numbers = [0] * (n + 1)

    # Initialize the first two Catalan numbers
    catalan_numbers[0], catalan_numbers[1] = 1, 1

    # Calculate the remaining Catalan numbers
    for i in range(2, n + 1):
        for j in range(i):
            catalan_numbers[i] = (catalan_numbers[i] + (catalan_numbers[j] * catalan_numbers[i - j - 1]) % MOD) % MOD

    return catalan_numbers[n]

# Test the function with the provided examples
test_cases_catalan = [3, 7, 1000]
results_catalan = [catalan(n) for n in test_cases_catalan]
print(results_catalan)

