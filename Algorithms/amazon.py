def distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy

def cercanas(index, stations):
    resultado = []
    for j in range(len(stations)):
        if j != index:
            d = distance(stations[index], stations[j])
            resultado.append((d, stations[j][0], stations[j][1], j))
    resultado.sort()
    return [resultado[0][3], resultado[1][3]]

def buildgrafos(stations):
    graph = []
    i = 0
    while i < len(stations):
        graph.append(cercanas(i, stations))
        i += 1
    return graph

def reachable(graph):
    n = len(graph)
    visited = [False] * n
    queue = [0]
    visited[0] = True
    front = 0
    while front < len(queue):
        node = queue[front]
        front += 1
        neighbors = graph[node]
        j = 0
        while j < len(neighbors):
            neighbor = neighbors[j]
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
            j += 1
    i = 0
    while i < n:
        if not visited[i]: return False
        i += 1
    return True

while True:
    try:
        line = input()
        if line == '':
            continue
        parts = line.split()
        if len(parts) == 0:
            continue
        N = int(parts[0])
        if N == 0:
            break
        coords = list(map(int, parts[1:]))
        while len(coords) < N*2:
            coords += list(map(int, input().split()))
        stations = []
        i = 0
        while i < len(coords):
            stations.append((coords[i], coords[i + 1]))
            i+=2
        graph = buildgrafos(stations)
        if reachable(graph):
            print("All stations are reachable.")
        else:
            print("There are stations that are unreachable.")
    except EOFError:
        break