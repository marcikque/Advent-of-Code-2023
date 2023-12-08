import math
import time
import re


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    print(f"\nPart 1: {part1(lines)}\nPart 2: {part2(lines)}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def part1(lines):
    instr = lines[0]
    nodes = {}
    for ln in lines[2:]:
        matches = re.findall(r'\b[A-Z]{3}\b', ln)
        nodes[matches[0]] = tuple(matches[1:])
    result = 0
    curr = 'AAA'
    while True:
        for c in instr:
            if c == 'L':
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]
            result += 1
            if curr[2] == 'Z':
                return result


def part2(lines):
    instr = lines[0]
    nodes = {}
    for ln in lines[2:]:
        matches = re.findall(r'\b[A-Z]{3}\b', ln)
        nodes[matches[0]] = tuple(matches[1:])
    results = []
    for k in nodes.keys():
        if k[2] == 'A':
            flag = True
            curr = k
            steps = 0
            while flag:
                for c in instr:
                    if c == 'L':
                        curr = nodes[curr][0]
                    else:
                        curr = nodes[curr][1]
                    steps += 1
                    if curr[2] == 'Z':
                        flag = False
                        results.append(steps)
                        steps = 0
                        break
    return math.lcm(*results)


if __name__ == "__main__":
    main()
