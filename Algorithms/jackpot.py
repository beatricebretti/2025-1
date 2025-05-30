def jackpot(bets, n):
    if n == 0: return "Losing streak."
    curr_max = 0
    max_global = 0
    for bet in bets:
        curr_max = max(0, curr_max + bet)
        max_global = max(max_global, curr_max)
    if max_global > 0:
        return f"The maximum winning streak is {max_global}."
    else:
        return "Losing streak."

def leer_input(n, buffer):
    numbers = []
    while len(numbers) < n:
        if not buffer:  
            try:
                line = input().strip()
                if line:
                    buffer.extend(map(int, line.split()))
            except EOFError: break
        while buffer and len(numbers) < n:
            numbers.append(buffer.pop(0))
    return numbers
buffer = []  
while True:
    try:
        line = input().strip()
        if not line:  continue
        n = int(line)
        if n == 0: break
        bets = leer_input(n, buffer)
        print(jackpot(bets, n))
    except EOFError: break