import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    histories = [[int(n) for n in ln.split()] for ln in lines]
    sol = solve(histories), solve([h[::-1] for h in histories])

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def solve(histories):
    result = 0
    for h in histories:
        levels = [h.copy()]
        while True:
            next_level = [levels[-1][i + 1] - levels[-1][i] for i in range(len(levels[-1]) - 1)]
            levels.append(next_level)
            if all(x == 0 for x in levels[-1]):
                break
        levels.reverse()
        levels[0].append(0)
        for i, lv in enumerate(levels[1:]):
            lv.append(levels[i][-1] + lv[-1])
        result += (levels[-1][-1])

    return result


if __name__ == "__main__":
    main()
