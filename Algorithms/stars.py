def dfs(grid, r, c, i, j, visited):
    if (i < 0 or i >= r or j < 0 or j >= c or visited[i][j] or grid[i][j] != '*'): return 0
    visited[i][j] = True
    count = 1  
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for di, dj in directions:
        count += dfs(grid, r, c, i + di, j + dj, visited)
    return count

def count_stars(r, c, grid):
    visited = [[False] * c for _ in range(r)]
    stars = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '*' and not visited[i][j]:
                component_size = dfs(grid, r, c, i, j, visited)
                if component_size == 1: stars += 1
    return stars

while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    grid = [input().strip() for _ in range(r)]
    result = count_stars(r, c, grid)
    print(result)

