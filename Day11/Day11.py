import itertools
import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = solve(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def solve(lines):
    universes = []
    for i, x in enumerate(lines):
        for j, y in enumerate(x):
            if y == '#':
                universes.append((i, j))  # row, col
    er, ec = set(), set()
    for i, ln in enumerate(lines):
        if '#' not in ln:
            er.add(i)
    for i, ln in enumerate(zip(*lines)):
        if '#' not in ln:
            ec.add(i)

    return expanded_manhattan(universes, er, ec, 1), expanded_manhattan(universes, er, ec, 999999)


def expanded_manhattan(universes, er, ec, expansion):
    result = 0
    grid = set()
    for (r, c) in universes:
        r_offset = len([x for x in er if x < r])
        c_offset = len([x for x in ec if x < c])
        adj_uni = (r + r_offset * expansion, c + c_offset * expansion)
        grid.add(adj_uni)

    pairs = list(itertools.combinations(grid, 2))

    for (a, b) in pairs:
        result += abs(a[0] - b[0]) + abs(a[1] - b[1])

    return result


if __name__ == "__main__":
    main()
