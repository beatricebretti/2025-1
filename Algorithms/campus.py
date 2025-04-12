import sys
import math

def distance(p1, p2):
    return math.sqrt((p2[0]- p1[0])**2 + (p2[1] - p1[1])**2)

def campus(points, num):
    distances = [0] 
    for i in range(1, len(points)):
        distances.append(distances[-1] + distance(points[i-1], points[i]))
    length = distances[-1]
    step = length / (num - 1)  
    positions = [points[0]]  
    current = step  

    i = 1  
    while len(positions) < num - 1:
        while current > distances[i]:
            i += 1
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        d1, d2 = distances[i-1], distances[i]
        ratio = (current - d1) / (d2 - d1)  
        new_x = x1 + ratio * (x2 - x1)
        new_y = y1 + ratio * (y2 - y1)
        positions.append((new_x, new_y))
        current += step  
    positions.append(points[-1])  
    return positions

data = sys.stdin.read().strip().split("\n")
i = 0
N = int(data[i])  
i += 1
results = []
for road in range(1, N + 1):
    K, T = map(int, data[i].split())
    i += 1
    points = []
    for _ in range(K):
        x, y = map(float, data[i].split())
        points.append((x, y))
        i += 1
    trees = campus(points, T)
    results.append(f"Road #{road}:")
    for x, y in trees:
        results.append(f"{x:.2f} {y:.2f}")
    results.append("")  
print("\n".join(results))
