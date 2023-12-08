import math
import time
import numpy as np


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = solve(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def solve(lines):
    r1, r2 = 0, np.ones(len(lines))
    for i, ln in enumerate(lines):
        lstr, rstr = ln.split(":")[1].split("|")
        winner = [int(number) for number in lstr.split()]
        mine = [int(number) for number in rstr.split()]
        intsct = len(set(winner) & set(mine))
        gain = np.array([0]*(i+1) + [1]*intsct)
        r1 += math.floor(2 ** (intsct - 1))
        gain = np.pad(gain[:len(lines)], (0, max(0, len(lines) - len(gain))), 'constant')
        r2 += r2[i] * gain

    return r1, int(sum(r2))


if __name__ == "__main__":
    main()
