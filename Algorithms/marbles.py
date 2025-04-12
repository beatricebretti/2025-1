import sys

def solve(n, c1, n1, c2, n2):
    min_cost = float('inf')
    best_m1, best_m2 = -1, -1
    for m1 in range(n // n1 + 1):
        remaining = n - m1 * n1
        if remaining % n2 == 0:
            m2 = remaining // n2
            cost = m1 * c1 + m2 * c2
            if cost < min_cost:
                min_cost = cost
                best_m1, best_m2 = m1, m2
    if best_m1 == -1:
        return "failed"
    return f"{best_m1} {best_m2}"


caso = sys.stdin.read().strip().split('\n')
index = 0
while index < len(caso):
    n = int(caso[index])
    if n == 0:
        break
    c1, n1 = map(int, caso[index + 1].split())
    c2, n2 = map(int, caso[index + 2].split())
    print(solve(n, c1, n1, c2, n2))
    index += 3

