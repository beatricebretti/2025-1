import sys
sys.setrecursionlimit(10000)

def is_valid(n, suffix):
    return str(n ** 3).endswith(suffix)

def backtrack(pos, digits, suffix):
    if pos == len(suffix):
        num = int(''.join(digits[::-1]))  
        if is_valid(num, suffix): return num
        return None
    for d in range(10):
        if pos == len(suffix) - 1 and d == 0: continue  
        digits.append(str(d))
        num = int(''.join(digits[::-1]))
        cube_suffix = str(num ** 3)[-pos - 1:]
        if cube_suffix == suffix[-pos - 1:]:
            res = backtrack(pos + 1, digits, suffix)
            if res is not None: return res
        digits.pop()
    return None

def solve(targets):
    results = []
    for suffix in targets:
        result = backtrack(0, [], suffix)
        results.append(str(result))
    return results

n = int(sys.stdin.readline())
targets = [sys.stdin.readline().strip() for _ in range(n)]
results = solve(targets)
for res in results:
    print(res)








