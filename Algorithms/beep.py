def calc_distancia(x1, y1, x2, y2):
    x_diff = x1 - x2
    if x_diff < 0: x_diff = -x_diff
    y_diff = y1 - y2
    if y_diff < 0: y_diff = -y_diff
    return x_diff + y_diff

def solve(x, y, coords, num):
    pos = [(0, 0)]*(num + 1)
    pos[0] = (x, y)
    for i in range(num):
        pos[i + 1] = coords[i]
    
    dist_list = []
    for i in range(num + 1):
        row = []
        for j in range(num + 1):
            dist = calc_distancia(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
            row.append(dist)
        dist_list.append(row)
    
    dp = []
    for i in range(1 << num):
        row = []
        for j in range(num + 1): row.append(float('inf'))
        dp.append(row)
    dp[0][0] = 0  
    
    for mask in range(1 << num):
        for curr in range(num + 1):
            if dp[mask][curr] == float('inf'): continue
            for next_beep in range(1, num + 1):
                index = next_beep-1  
                if (mask & (1 << index)) == 0:  
                    new_mask=mask | (1 << index)
                    new_dist = dp[mask][curr] + dist_list[curr][next_beep]
                    if new_dist < dp[new_mask][next_beep]:
                        dp[new_mask][next_beep] = new_dist
    
    full_mask = (1 << num) - 1
    min_dist = float('inf')
    for last in range(1, num+1):
        if dp[full_mask][last] != float('inf'):
            dist_start = dp[full_mask][last] + dist_list[last][0]
            if dist_start < min_dist:
                min_dist = dist_start
    return min_dist

num = int(input())
for scenario in range(num):
    n = input().split()
    x_size = int(n[0])
    y_size = int(n[1])
    start = input().split()
    x = int(start[0])
    y = int(start[1])
    num_beep = int(input())
    coords = []
    for i in range(num_beep):
        beeper_input = input().split()
        beeper_x = int(beeper_input[0])
        beeper_y = int(beeper_input[1])
        coords.append((beeper_x, beeper_y))
    result = solve(x, y, coords, num_beep)
    print("The shortest path has length", result)
