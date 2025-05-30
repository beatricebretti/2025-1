def primes(limit):
    filtro = [True]* (limit+1)
    filtro[0] = filtro[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if filtro[i]:
            for j in range(i * i, limit + 1, i):
                filtro[j] = False
    result = []
    for i in range(limit+1):
        if filtro[i]:
            result.append(i)
    return result

def solve_dp(primes, max_n, max_k):
    dp = []
    for _ in range(max_n + 1):
        row = []
        for _ in range(max_k + 1):
            row.append(0)
        dp.append(row)
    dp[0][0] = 1
    for prime in primes:
        for i in range(max_n, prime-1, -1):
            for j in range(max_k, 0, -1):
                dp[i][j] += dp[i-prime][j-1]
    return dp

primos = primes(1120)
dp = solve_dp(primos, 1120, 14)
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0: break
    print(dp[n][k])