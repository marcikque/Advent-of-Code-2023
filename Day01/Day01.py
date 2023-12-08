import time


def main():
    start = time.time()
    with open('input.txt', 'r') as file:
        lines = [ln.strip() for ln in file]

    sol = part1(lines), part2(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time: {(time.time() - start) * 1000:.4f} ms")


def part1(lines):
    result = 0
    for ln in lines:
        digits = [el for el in ln if el.isdigit()]
        result += (int(digits[0] + digits[-1]))
    return result


def part2(lines):
    result = 0
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for ln in lines:
        digits = []
        for i, c in enumerate(ln):
            if c.isdigit():
                digits.append(c)
            else:
                for j, n in enumerate(numbers):
                    if ln[i:i+(len(n))] == n:
                        digits.append(str(j))
        result += (int(digits[0] + digits[-1]))
    return result


if __name__ == "__main__":
    main()
