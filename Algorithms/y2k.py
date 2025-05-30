def calcsurplus(s, d):
    def dfs(month, record):
        if month == 12:
            i = 0
            while i <= 7:
                total = 0
                j = i
                while j < i + 5:
                    total += record[j]
                    j += 1
                if total >= 0:
                    return -1
                i += 1
            year_total = 0
            k = 0
            while k < 12:
                year_total += record[k]
                k += 1
            return year_total
        record.append(s)
        a = dfs(month + 1, record)
        record.pop()
        record.append(-d)
        b = dfs(month + 1, record)
        record.pop()
        return max(a, b)
    
    result = dfs(0, [])
    if result < 0:
        return "Deficit"
    return result

try:
    while True:
        line = input()
        if line == "":
            continue
        parts = line.split()
        s = int(parts[0])
        d = int(parts[1])
        print(calcsurplus(s, d))
except EOFError:
    pass