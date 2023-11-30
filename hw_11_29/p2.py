def catalan(n):
    MOD = 10**9 + 7

    if n <= 1:
        return 1

    catalan_numbers = [0] * (n + 1)
    catalan_numbers[0], catalan_numbers[1] = 1, 1

    for i in range(2, n + 1):
        for j in range(i):
            catalan_numbers[i] = (catalan_numbers[i] + (catalan_numbers[j] * catalan_numbers[i - j - 1]) % MOD) % MOD

    return catalan_numbers[n]

# test cases
test_cases_catalan = [3, 7, 1000]
results_catalan = [catalan(n) for n in test_cases_catalan]
print(results_catalan)

