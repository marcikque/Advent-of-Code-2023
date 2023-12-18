import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = part1(lines), part2(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def part1(lines):
    transpose = [''.join(s) for s in zip(*lines)]
    result = 0
    for x in transpose:
        parts = x.split("#")
        ctr = len(x)
        for p in [''.join(sorted(k, reverse=True)) for k in parts]:
            last = p.rfind('O') + 1
            result += ctr * last - (last - 1) * last // 2
            ctr -= len(p) + 1
    return result


def part2(lines):
    result = 0
    grid = lines
    seen = [grid]
    while True:
        for _ in range(4):
            grid = map("".join, zip(*grid))
            grid = ["#".join(["".join(sorted(group, reverse=True)) for group in row.split("#")]) for row in grid]
            grid = [row[::-1] for row in grid]

        if grid in seen:
            break
        seen.append(grid)

    idx = seen.index(grid)
    itr = (1000000000 - idx) % (len(seen) - idx)
    grid = seen[idx + itr]
    for i, x in enumerate(grid):
        result += (len(grid) - i) * len([c for c in x if c == 'O'])
    return result


if __name__ == "__main__":
    main()
