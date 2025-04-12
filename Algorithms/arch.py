import sys

def arch(N):
    cant_N = len(str(N))
    E = 1
    max_iterations = 100000  
    while E <= max_iterations:
        v2E = 2**E
        cant_v2E = len(str(v2E))
        divisor = 10 ** (abs(cant_v2E - cant_N))
        digitos = v2E // divisor
        if (cant_v2E >= (cant_N + cant_N + 1)) and digitos == N:
            return E
        E += 1
    return "no power of 2"

for line in sys.stdin:
    N = line.strip()
    if not N: 
        continue
    print(arch(int(N)))
  



