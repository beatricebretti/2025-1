import sys

def calcmoves(arr):
    colors = ['B', 'G', 'C'] 
    bins = [(arr[0], arr[1], arr[2]), (arr[3], arr[4], arr[5]), (arr[6], arr[7], arr[8])]
    orders = [ (0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    moves = float('inf')
    best = ""
    for order in orders: 
        count = 0
        for i in range(3):
            count += sum(bins[i]) - bins[i][order[i]]
        order_str = ''.join(colors[i] for i in order)
        if count < moves or (count == moves and order_str < best):
            moves = count
            best = order_str
    return best, moves

for line in sys.stdin:
    num = list(map(int, line.split()))
    order, moves = calcmoves(num)
    print(order, moves)