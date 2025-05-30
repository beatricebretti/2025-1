import heapq

def solve(n, inicial, graph):
    dist = [float('inf')] * (n + 1)
    dist[inicial] = 0
    pq = [(0, inicial)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v]=dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

t = int(input())
vacia = input()
for i in range(t):
    n = int(input())
    e = int(input())
    T= int(input())
    m = int(input())
    graph = [[] for i in range(n + 1)]
    for j in range(m):
        a, b, time = map(int, input().split())
        graph[b].append((a, time))
    dist = solve(n, e, graph)

    count = sum(1 for i in range(1, n + 1) if dist[i] <= T)
    print(count)
    if i < t - 1:
        input()




