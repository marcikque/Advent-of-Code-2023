import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = file.readline().split(',')

    sol = part1(lines), part2(lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def part1(lines):
    result = 0
    for x in [ln.strip("\n") for ln in lines]:
        result += hashing(x)
    return result


def part2(lines):
    result = 0
    boxes, lengths = {}, {}
    for x in [ln.strip("\n") for ln in lines]:
        if '=' in x:
            label, focal = x.split("=")
            focal = int(focal)
            num = hashing(label)
            if num not in boxes:
                boxes[num] = []
            if label not in boxes[num]:
                boxes[num].append(label)

            lengths[label] = focal
        else:
            label = x[:-1]
            num = hashing(label)
            if num in boxes and label in boxes[num]:
                boxes[num].remove(label)

    for k, v in boxes.items():
        result += sum([(k + 1) * (i + 1) * lengths[label] for i, label in enumerate(v)])
    return result


def hashing(label):
    curr = 0
    for c in label:
        curr = (curr + ord(c)) * 17 % 256
    return curr


if __name__ == "__main__":
    main()
