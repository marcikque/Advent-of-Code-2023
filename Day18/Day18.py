import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = solve(lines, False), solve(lines, True)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def solve(lines, hexa):
    dug = [(0, 0)]
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    LUT = "RDLU"
    x, y = 0, 0
    border = 0
    for ln in lines:
        a, b, c = ln.split()
        a = LUT.index(a)
        b = int(b)
        if hexa:
            a = int(c[-2])
            b = int(c[2:7], 16)

        x, y = x + directions[a][0] * b, y + directions[a][1] * b
        dug.append((x, y))
        border += b

    # Gauss' Area = \frac{1}{2}\vert\sum\limits_{i=1}^{n} (x_{i} \cdot y_{i+1} - x_{i+1} \cdot y_{i})\vert
    interior = 0.0
    for x in range(len(dug)):
        y = (x + 1) % len(dug)
        interior += dug[x][0] * dug[y][1] - dug[y][0] * dug[x][1]
    interior = abs(interior) / 2.0
    # Pick's Area = I + \frac{B}{2} - 1
    result = interior + border / 2 + 1
    return int(result)


if __name__ == "__main__":
    main()
