from collections import defaultdict

def has_cycle(graph, node, visited, rec_stack):
    visited[node] = True
    rec_stack[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
    rec_stack[node] = False
    return False

def detect_cycle(graph, nodes):
    visited = {node: False for node in nodes}
    rec_stack = {node: False for node in nodes}
    for node in nodes:
        if not visited[node]:
            if has_cycle(graph, node, visited, rec_stack):
                return True
    return False

def sorts(graph, in_degree, nodes, used, path, results):
    candidates = [node for node in nodes if in_degree[node] == 0 and not used[node]]
    
    if not candidates and len(path) == len(nodes):
        results.append(' '.join(path))
        return
    
    for node in sorted(candidates):  
        used[node] = True
        path.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
        sorts(graph, in_degree, nodes, used, path, results)
        used[node] = False
        path.pop()
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

def solve(variables, constraints):
    graph = defaultdict(list)
    in_degree = {v: 0 for v in variables}
    for a, b in constraints:
        graph[a].append(b)
        in_degree[b] += 1
    
    if detect_cycle(graph, variables): return ["NO"]
    used = {v: False for v in variables}
    path = []
    results = []
    sorts(graph, in_degree, variables, used, path, results)
    return sorted(results) if results else ["NO"]

t = int(input())
for case in range(t):
    input()  
    variables = input().strip().split()
    constraints = [c.split('<') for c in input().strip().split()]
    constraints = [(a.strip(), b.strip()) for a, b in constraints]
    results = solve(variables, constraints)
    for result in results:
        print(result)
    if case < t - 1:
        print()

