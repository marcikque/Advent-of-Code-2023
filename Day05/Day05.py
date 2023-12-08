import math
import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = file.read().split("\n\n")

    sol = part1(lines), part2(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def part1(lines):
    seeds = [int(number) for number in lines[0].split(":")[1].split()]
    for block in lines[1:]:
        mapping = []
        while seeds:
            curr = seeds.pop()
            for ln in block.split("\n")[1:]:
                lims = [int(num) for num in ln.split()]
                if lims[1] <= curr < lims[1] + lims[2]:
                    mapping.append(lims[0] + abs(curr - lims[1]))
                    break
            else:
                mapping.append(curr)
        seeds = mapping.copy()
    return min(seeds)


def part2(lines):
    seeds = [int(number) for number in lines[0].split(":")[1].split()]
    seeds = list(zip(seeds[::2], seeds[1::2]))
    for block in lines[1:]:
        mapping = []
        while seeds:
            a, b = seeds.pop()
            for ln in block.split("\n")[1:-1]:
                lims = [int(num) for num in ln.split()]
                l, r = max(a, lims[1]), min(b, lims[1] + lims[2])
                if l < r:
                    mapping.append((l - lims[1] + lims[0], r - lims[1] + lims[0]))
                    if l > a:
                        seeds.append((a, l))
                    if b > r:
                        seeds.append((r, b))
                    break
            else:
                mapping.append((a, b))
        seeds = mapping.copy()
    return min(seeds)[0]


if __name__ == "__main__":
    main()
