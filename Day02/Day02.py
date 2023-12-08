import re
import time


def main():
    start = time.time()
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]

    sol = solve(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time: {(time.time() - start) * 1000:.4f} ms")


def solve(lines):
    r1, r2 = 0, 0
    for i, ln in enumerate(lines):
        flag, temp = True, 1
        for j, color in enumerate(["red", "green", "blue"]):
            cubes = [int(n.split()[0]) for n in re.findall(r'\d+ ' + color, ln)]
            temp *= max(cubes)
            if max(cubes) > j + 12:
                flag = False
        if flag:
            r1 += i + 1
        r2 += temp
    return r1, r2


if __name__ == "__main__":
    main()
