def find_digit(i):
    if i <= 0: return 0
    
    def find_group(pos):
        digits = 0
        k = 0
        while digits < pos:
            k += 1
            for num in range(1, k + 1):
                digits += len(str(num))
            if digits >= pos: return k, digits
        return k, digits
    
    k, total_digits = find_group(i)
    
    def find_groupdig(pos, group):
        digits_so_far = 0
        for g in range(1, group):
            for num in range(1, g + 1):
                digits_so_far += len(str(num))
        remaining_pos = pos - digits_so_far
        for num in range(1, group + 1):
            num_str = str(num)
            if remaining_pos <= len(num_str):
                return int(num_str[remaining_pos - 1])
            remaining_pos -= len(num_str)
        return 0
    return find_groupdig(i, k)

t = int(input())  
for _ in range(t):
    i = int(input())
    print(find_digit(i))


