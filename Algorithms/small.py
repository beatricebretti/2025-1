import math

def solve(m):
    if m == 0:
        return
    minimo = float('inf')
    log3 = math.log(3)
    log2 = math.log(2)
    logm = math.log(m)
    
    for i in range(32):  
        j = math.ceil((logm -i * log2) / log3)
        if j < 0:
            j = 0  
        n = (1 <<i) * (3 ** j)  
        if n >= m:
            minimo = min(minimo, n)
    return minimo

while True:
    m = int(input())
    if m == 0:
        break
    print(solve(m))