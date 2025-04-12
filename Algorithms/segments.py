import sys

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def verify(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def intersect(p1, c1, p2, c2):
    o1 = orientation(p1, c1, p2)
    o2 = orientation(p1, c1, c2)
    o3 = orientation(p2, c2, p1)
    o4 = orientation(p2, c2, c1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and verify(p1, p2, c1): return True
    if o2 == 0 and verify(p1, c2, c1): return True
    if o3 == 0 and verify(p2, p1, c2): return True
    if o4 == 0 and verify(p2, c1, c2): return True
    return False

def segments(cases):
    results = []
    for segments in cases:
        n = len(segments)
        count = 0
        for i in range(n):
            isolated = True
            for j in range(n):
                if i != j and intersect(segments[i][0], segments[i][1], segments[j][0], segments[j][1]):
                    isolated = False
                    break
            if isolated:
                count += 1
        results.append(count)
    return results

input = sys.stdin.read
data = input().splitlines()
i = 0
N = int(data[i])
i += 1
cases = []
for _ in range(N):
    M = int(data[i])
    i += 1
    segment = []
    for _ in range(M):
        x1, y1, x2, y2 = map(int, data[i].split())
        segment.append(((x1, y1), (x2, y2)))
        i += 1
    cases.append(segment)
results = segments(cases)
for res in results:
    print(res)




