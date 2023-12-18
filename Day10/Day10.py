import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = solve(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def solve(lines):
    grid = {}
    for y, ln in enumerate(lines):
        for x, c in enumerate(ln):
            grid[(x, y)] = c

    sx, sy = [k for k, v in grid.items() if v == 'S'][0]
    visited = {(sx, sy)}

    neighbors = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    LUT1 = ["|7F", "-J7", "|LJ", "-FL"]

    queue = []
    for i, (dx, dy) in enumerate(neighbors):
        cx, cy = sx + dx, sy + dy
        if (cx, cy) in grid and grid[(cx, cy)] in LUT1[i]:
            queue.append((cx, cy))
            visited.add((cx, cy))

    while queue:
        cx, cy = queue.pop(0)
        for i, (dx, dy) in enumerate(neighbors):
            if grid[(cx, cy)] not in LUT1[(i + 2) % 4]:
                continue
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in grid and grid[(nx, ny)] in LUT1[i]:
                if (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))

    result = 0
    for y, ln in enumerate(lines):
        for x, c in enumerate(ln):
            if (x, y) not in visited:
                crosses = 0
                nx, ny = x, y
                while (nx, ny) in grid:
                    if (nx, ny) in visited and grid[(nx, ny)] not in "L7":
                        crosses += 1
                    nx, ny = nx + 1, ny + 1
                result += crosses % 2

    return len(visited) // 2, result


if __name__ == "__main__":
    main()
