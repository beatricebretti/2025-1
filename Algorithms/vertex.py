def dfs(graph, start, visited, n):
    visited[start-1] = True
    for neighbor in graph[start-1]:
        if not visited[neighbor-1]:
            dfs(graph, neighbor, visited, n)

def solve_case(n, edges, queries):
    # Initialize adjacency list
    graph = [[] for _ in range(n)]
    for start, ends in edges:
        for end in ends:
            graph[start-1].append(end)
    
    results = []
    for start in queries:
        # Run DFS to find reachable vertices
        visited = [False] * n
        dfs(graph, start, visited, n)
        # Collect inaccessible vertices
        inaccessible = [i+1 for i in range(n) if not visited[i]]
        # Format output: count followed by vertices
        result = [len(inaccessible)] + inaccessible
        results.append(' '.join(map(str, result)))
    return results

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        # Read edges
        edges = []
        while True:
            line = list(map(int, input().split()))
            if line == [0]:
                break
            start = line[0]
            ends = line[1:-1]  # Exclude the trailing 0
            edges.append((start, ends))
        # Read queries
        query_line = list(map(int, input().split()))
        num_queries = query_line[0]
        queries = query_line[1:num_queries+1]
        # Solve case
        results = solve_case(n, edges, queries)
        # Output results
        for result in results:
            print(result)

if __name__ == "__main__":
    main()