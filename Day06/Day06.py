import time
from math import sqrt, ceil


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = part1(lines), part2(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def part1(lines):
    durs = [int(x) for x in lines[0].split(":")[1].split()]
    dists = [int(x) for x in lines[1].split(":")[1].split()]

    result = 1
    for t, d in zip(durs, dists):
        wins = 0
        for i in range(t):
            if (t-i) * i > d:
                wins += 1
        result *= wins
    return result


def part2(lines):
    dur = int(lines[0].split(":")[1].replace(" ", ""))
    dist = int(lines[1].split(":")[1].replace(" ", ""))

    s = sqrt(((dur ** 2) / 4) - dist)
    r1, r2 = dur / 2 - s, dur / 2 + s

    return ceil(r2) - ceil(r1)


if __name__ == "__main__":
    main()
