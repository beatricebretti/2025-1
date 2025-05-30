import math

def f(x, p, q, r, s, t, u):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u

def solve(p, q, r, s, t, u):
    left, right = 0.0, 1.0
    eps = 1e-6  
    f_left = f(left, p, q, r, s, t, u)
    f_right = f(right, p, q, r, s, t, u)

    if f_left * f_right > 0: return "No solution"

    while right - left > eps:
        mid = (left + right) / 2
        f_mid = f(mid, p, q, r, s, t, u)
        if abs(f_mid) < eps:
            return f"{mid:.4f}"
        elif f_mid * f(left, p, q, r, s, t, u) < 0:
            right = mid  
        else:
            left = mid  
    return f"{left:.4f}"

while True:
    try:
        p, q, r, s, t, u = map(int, input().split())
        print(solve(p, q, r, s, t, u))
    except EOFError:
        break

