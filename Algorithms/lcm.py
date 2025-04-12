import sys
import itertools
import math

def lcm(N):
    factors = list(range(1, N + 1))
    min_sum = float('inf')
    best = None
    for i in itertools.combinations(factors, 2):
        if math.lcm(*i) == N:
            current = sum(i)
            if current < min_sum:
                min_sum = current
                best = i
    return min_sum

casenum = 1
for line in sys.stdin:
    N = int(line.strip())
    if N == 0:
        break
    print(f"Case {casenum}: {lcm(N)}")
    casenum += 1


