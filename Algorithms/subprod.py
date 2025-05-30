while True:
    try:
        seq = list(map(int, input().split()))
    except EOFError:
        break  

    #caso base
    if not seq or seq[0] == -999999:  break
    seq = seq[:-1] if seq[-1] == -999999 else seq
    if not seq:  continue
        
    max_actual = seq[0]  
    max_now = seq[0]  
    min_now = seq[0]  
    
    for i in range(1, len(seq)):
        num = seq[i]
        if num == 0:
            max_now = 0
            min_now = 0
        elif num > 0:
            max_now = max(num, max_now * num)
            min_now = min(num, min_now * num)
        else:  
            temp_max = max_now
            max_now = max(num, min_now * num)
            min_now = min(num, temp_max * num)
        max_actual = max(max_actual, max_now)
    print(max_actual)