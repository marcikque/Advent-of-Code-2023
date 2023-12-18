import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = part1(lines), part2(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def part1(lines):
    start = ((0, 0), 1)
    return laser(start, lines)


def laser(start, lines):
    grid = {}
    for y, ln in enumerate(lines):
        for x, c in enumerate(ln):
            grid[(x, y)] = c

    activated = set()  # format: (y,x)
    entries_visited = {start}  # format: ((y,x), dir) dir: 0,1,2,3 top-left clockwise
    queue = [start]

    while queue:
        ((x, y), d) = queue.pop(0)
        if (x,y) in grid:
            sym = grid[(x, y)]
            match sym:
                case '/':
                    new_dir = [abs(d - 1)] if d in [0, 1] else [abs(d - 5)]
                case '\\':
                    new_dir = [abs(d - 3)]
                case '-':
                    new_dir = [1, 3] if d in [0, 2] else [d]
                case '|':
                    new_dir = [0, 2] if d in [1, 3] else [d]
                case _:
                    new_dir = [d]

            activated.add((x, y))
            tr_coord = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            for n in new_dir:
                new_coord = (tr_coord[n][0] + x, tr_coord[n][1] + y)
                new_el = (new_coord, n)
                if new_el not in entries_visited:
                    queue.append(new_el)
                    entries_visited.add(new_el)
    return len(activated)


def part2(lines):
    results = set()
    for i, x in enumerate(lines):
        if i == 0:
            results.update({laser(((k, i), 2), lines) for k in range(len(x))})

        if i == len(lines) - 1:
            results.update({laser(((k, i), 0), lines) for k in range(len(x))})

        results.add(laser(((0, i), 1), lines))
        results.add(laser(((len(x) - 1, i), 3), lines))

    return max(results)


if __name__ == "__main__":
    main()
