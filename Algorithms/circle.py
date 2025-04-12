import sys
import math

def circle(x1, y1, x2, y2, x3, y3):
    A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
    if A == 0:
        return None
    
    B = (x1**2+y1**2)*(y3-y2)+(x2**2+y2**2)*(y1-y3)+(x3**2+y3**2)*(y2 -y1)
    C = (x1**2+y1**2)*(x2-x3)+(x2**2+y2**2)*(x3-x1)+(x3**2+y3**2)*(x1 - x2)
    D = (x1**2+y1**2)*(x3*y2-x2*y3)+(x2**2+y2**2)*(x1*y3-x3*y1)+(x3**2+y3**2)*(x2*y1-x1*y2)
    h = -B / (2 * A)
    k = -C / (2 * A)
    r2 = (h - x1) ** 2 + (k - y1) ** 2
    r = math.sqrt(r2)
    c = -2 * h
    d = -2 * k
    e = h**2 + k**2 - r2

    #y si alguno es 0?----
    # circuloo
    circle = []
    if h != 0:
        circle.append(f"(x {'-' if h > 0 else '+'} {abs(h):.3f})^2")
    else:
        circle.append("x^2")
    if k != 0:
        circle.append(f"+ (y {'-' if k > 0 else '+'} {abs(k):.3f})^2")
    else:
        circle.append("+ y^2")
    circle.append(f"= {r:.3f}^2")
    print(" ".join(circle))
    # genral
    gral = ["x^2", "+ y^2"]
    if c != 0:
        gral.append(f"{'-' if c < 0 else '+'} {abs(c):.3f}x")
    if d != 0:
        gral.append(f"{'-' if d < 0 else '+'} {abs(d):.3f}y")
    if e != 0:
        gral.append(f"{'-' if e < 0 else '+'} {abs(e):.3f}")
    gral.append("= 0")
    print(" ".join(gral) + "\n")

for line in sys.stdin:
    data = list(map(float, line.split()))
    circle(*data)

