from itertools import product
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def valid_primes(digit_sum):
    valid = []
    for n in range(10000, 100000):
        if is_prime(n) and sum(int(d) for d in str(n)) == digit_sum:
            valid.append(str(n))
    return valid

def solve(digit_sum, start_digit):
    primes = valid_primes(digit_sum)
    prefix_map = {}
    for p in primes:
        for i in range(6):
            prefix = p[:i]
            prefix_map.setdefault(prefix, []).append(p)
    solutions = []

    def backtrack(grid):
        if len(grid) == 5:
            cols = [''.join(row[i] for row in grid) for i in range(5)]
            diag1 = ''.join(grid[i][i] for i in range(5))
            diag2 = ''.join(grid[i][4 - i] for i in range(5))
            all_lines = grid + cols + [diag1, diag2]
            if all(is_prime(int(line)) and sum(int(d) for d in line) == digit_sum for line in all_lines):
                solutions.append(grid.copy())
            return
        row_idx = len(grid)
        for p in primes:
            if row_idx == 0 and p[0] != str(start_digit): continue
            valid = True
            for col in range(5):
                prefix = ''.join(grid[r][col] for r in range(row_idx)) + p[col]
                if prefix not in prefix_map:
                    valid = False
                    break
            if not valid: continue
            if row_idx < 5:
                d1 = ''.join(grid[i][i] for i in range(row_idx)) + p[row_idx]
                d2 = ''.join(grid[i][4 - i] for i in range(row_idx)) + p[4 - row_idx]
                if d1 not in prefix_map or d2 not in prefix_map: continue
            grid.append(p)
            backtrack(grid)
            grid.pop()
    backtrack([])
    for square in sorted(solutions):
        for row in square:
            print(row)
        print()

d_sum = int(input())
sdigit = int(input())
solve(d_sum, sdigit)