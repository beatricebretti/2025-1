def to_d(r1, r2, c1, c2, bitmap):
    same = True
    first = bitmap[r1][c1]
    i = r1
    while i < r2:
        j = c1
        while j < c2:
            if bitmap[i][j] != first:
                same = False
                break
            j += 1
        if not same:
            break
        i += 1
    if same:
        return first
    else:
        result = "D"
        top = r2 - r1
        left = c2 - c1
        rmid = r1 + top // 2 + (top % 2)
        cmid = c1 + left // 2 + (left % 2)
        result += to_d(r1, rmid, c1, cmid, bitmap)
        result += to_d(r1, rmid, cmid, c2, bitmap)
        result += to_d(rmid, r2, c1, cmid, bitmap)
        result += to_d(rmid, r2, cmid, c2, bitmap)
        return result

def to_b(dstr, idx, rows, cols):
    def fill(r1, r2, c1, c2):
        nonlocal idx
        ch = dstr[idx]
        idx += 1
        if ch == "0" or ch == "1":
            i = r1
            while i < r2:
                j = c1
                while j < c2:
                    result[i][j] = ch
                    j += 1
                i += 1
        else:
            top = r2 - r1
            left = c2 - c1
            rmid = r1 + top // 2 + (top % 2)
            cmid = c1 + left // 2 + (left % 2)
            fill(r1, rmid, c1, cmid)
            fill(r1, rmid, cmid, c2)
            fill(rmid, r2, c1, cmid)
            fill(rmid, r2, cmid, c2)
    result = [["0"] * cols for _ in range(rows)]
    fill(0, rows, 0, cols)
    return result

def solve(bitmaps):
    for mode, rows, cols, data in bitmaps:
        print()
        if mode == "B":
            bitmap = []
            i = 0
            while i < rows:
                row = data[i * cols:(i + 1) * cols]
                bitmap.append(list(row))
                i += 1
            transf = to_d(0, rows, 0, cols, bitmap)
            print("D{:>4}{:>4}".format(rows, cols))
            i = 0
            while i < len(transf):
                print(transf[i:i+50])
                i += 50
        else:
            ind = 0
            result = to_b(data, ind, rows, cols)
            normal = "".join("".join(row) for row in result)
            print("B{:>4}{:>4}".format(rows, cols))
            i = 0
            while i < len(normal):
                print(normal[i:i+50])
                i += 50

bitmaps = []
while True:
    line = input()
    if line == "#":
        break
    parts = line.split()
    mode = parts[0]
    rows = int(parts[1])
    cols = int(parts[2])
    data = ""
    while len(data)<rows * cols if mode == "B" else True:
        part = input().strip()
        if part == "" or part == "#" or part[0] in "BD":
            break
        data += part
        if len(data) >= rows * cols and mode == "B":
            break
    bitmaps.append((mode, rows, cols, data))
solve(bitmaps)