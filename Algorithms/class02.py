# Memoization: optimizar guardando resultados
# fibonacci:, f(0) = 0, f(1) = 1, f(n) = b(
# se puede usar con decorators, con clase

import sys

def arch(N):
    cant_N = len(str(N))
    E = 1
    max_iterations = 100000  

    while E <= max_iterations:
        v2E = 2**E
        cant_v2E = len(str(v2E))

        # Ensure divisor is only applied when cant_v2E >= cant_N
        if cant_v2E >= cant_N:
            divisor = 10 ** (cant_v2E - cant_N)  # Extract first cant_N digits
            digitos = v2E // divisor  

            if digitos == N:
                return E

        E += 1
    
    return "no power of 2"

for line in sys.stdin:
    N = line.strip()
    if not N: 
        continue
    print(arch(int(N)))





