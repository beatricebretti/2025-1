def solve(weights, target):
    dp = [False] *(target + 1)
    dp[0] = True
    for w in weights:
        for j in range(target, w - 1, -1):
            if dp[j - w]: dp[j] = True
    return dp[target]


m = int(input())
for _ in range(m):
    weights = list(map(int, input().split()))
    total_sum = sum(weights)
    if total_sum % 2 != 0:
        print("NO")
    else:
        target = total_sum // 2
        if solve(weights, target):
            print("YES")
        else:
            print("NO")

