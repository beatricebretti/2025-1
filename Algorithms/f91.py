def f91(N):
    if N == 91:
        return N
    elif N <= 100:
        return f91(f91(N+11))
    if N >= 101:
        return N-10

while True:
    N = int(input())
    if N == 0:
        break
    print(f"f91({N}) = {f91(N)}")
