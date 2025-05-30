from collections import defaultdict
import heapq

def solve(graph, start, end, vertices):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    pq = [(0, 0, start, [start])]
    visited = set()
    
    while pq:
        cost, nodes, current, path = heapq.heappop(pq)
        if current in visited: continue
        visited.add(current)
        if current == end: return path
            
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_cost = cost + weight
                new_nodes = nodes + 1
                if new_cost < dist[neighbor] or (new_cost == dist[neighbor] and new_nodes < dist[neighbor + '_nodes']):
                    dist[neighbor] = new_cost
                    dist[neighbor + '_nodes'] = new_nodes
                    new_path = path + [neighbor]
                    heapq.heappush(pq, (new_cost, new_nodes, neighbor, new_path))
    return []

s, p = map(int, input().split())
graph = defaultdict(list)
vertices = set()
for _ in range(p):
    u, v, w = input().split()
    w = int(w)
    graph[u].append((v, w))
    graph[v].append((u, w))  
    vertices.add(u)
    vertices.add(v)
n = int(input())
queries = []
for _ in range(n):
    start, end = input().split()
    queries.append((start, end))
for start, end in queries:
    path = solve(graph, start, end, vertices)
    print(' '.join(path))

