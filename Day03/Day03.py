import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = solve(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time: {(time.time() - start) * 1000:.4f} ms")


def solve(lines):
    r1 = r2 = 0
    gears = {}
    for i, ln in enumerate(lines):
        num = ""
        flag = False
        gearAdj = (-1, -1)
        for j, c in enumerate(ln):
            if c.isdigit():
                num += c
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        if 0 < i + a < len(lines) and 0 < j + b < len(ln):
                            if lines[i + a][j + b] != '.' and not lines[i + a][j + b].isdigit():
                                flag = True
                                if lines[i + a][j + b] == '*':
                                    gearAdj = (i + a, j + b)
            if not c.isdigit() or j == len(ln) - 1:
                if len(num) > 0 and flag:
                    r1 += int(num)
                    if gearAdj != (-1, -1):
                        if gearAdj not in gears.keys():
                            gears[gearAdj] = []
                        gears[gearAdj].append(int(num))
                gearAdj = (-1, -1)
                flag = False
                num = ""
    for gear, coords in gears.items():
        if len(coords) > 1:
            ratio = 1
            for coord in coords:
                ratio *= coord
            r2 += ratio
    return r1, r2


if __name__ == "__main__":
    main()
