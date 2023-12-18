import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        blocks = file.read().split("\n\n")

    sol = solve(blocks, exact), solve(blocks, smear)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def solve(blocks, comparison):
    result = 0
    for block in blocks:
        rows1 = block.splitlines()
        rows2 = (list(zip(*rows1)))
        result += compare(rows1, comparison) * 100 + compare(rows2, comparison)
    return result


def compare(rows, comparison):
    for r in range(1, len(rows)):
        right = rows[:r][::-1][:len(rows) - r]
        left = rows[r:][:len(right)]

        if comparison(left, right):
            return r
    return 0


def exact(left, right):
    return left == right


def smear(left, right):
    pairs = ((a, b) for x, y in zip(left, right) for a, b in zip(x, y))
    return len([(x, y) for (x, y) in pairs if x != y]) == 1


if __name__ == "__main__":
    main()
