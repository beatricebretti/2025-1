from collections import deque

def find_cycles(n, adj):
    visited = [0] * n  
    cycle_id = [-1] * n
    cycle_sizes = []
    current_cycle = 0
    stack = []
    
    def dfs(u):
        nonlocal current_cycle
        visited[u] = 1  
        stack.append(u)
        v = adj[u]
        
        if visited[v] == 0:  
            dfs(v)
        elif visited[v] == 1: 
            cycle = []
            cycle_start = v
            while stack[-1] != v:
                cycle.append(stack.pop())
            cycle.append(v)
            stack.pop()
            cycle_size = len(cycle)
            cycle_sizes.append(cycle_size)
            for node in cycle:
                cycle_id[node] = current_cycle
            current_cycle += 1
        
        if stack and stack[-1] == u: stack.pop()
        visited[u] = 2  
    
    for u in range(n):
        if visited[u] == 0: dfs(u)
    
    reach = [0] * n
    for u in range(n):
        visited = [False] * n
        stack = deque([u])
        visited[u] = True
        count = 1
        while stack:
            curr = stack.popleft()
            next_node = adj[curr]
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)
                count += 1
        reach[u] = count
    
    max_reach = max(reach)
    best_node = min(i + 1 for i in range(n) if reach[i] == max_reach)
    return best_node

def solve_case(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u-1] = v-1
    return find_cycles(n, adj)

t = int(input())
for case in range(1, t+1):
    n = int(input())
    edges = []
    for _ in range(n):
        u, v = map(int, input().split())
        edges.append((u, v))
    result = solve_case(n, edges)
    print(f"Case {case}: {result}")

