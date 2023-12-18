import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = solve(lines, False), solve(lines, True)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def rec(ln, grp, mem):
    if (ln, grp) in mem:
        return mem[(ln, grp)]

    match (ln, grp):
        case ('', ()): return 1
        case ('', _): return 0
        case (_, ()): return 0 if '#' in ln else 1
        case _: pass

    cnt = 0
    if ln[0] != '#':
        cnt += rec(ln[1:], grp, mem)
    if ln[0] != '.':
        if len(ln) >= grp[0] and '.' not in ln[:grp[0]] and (len(ln) == grp[0] or ln[grp[0]] != '#'):
            cnt += rec(ln[grp[0] + 1:], grp[1:], mem)

    mem[(ln, grp)] = cnt
    return cnt


def solve(lines, fivefold):
    result = 0
    mem = {}
    for i, ln in enumerate(lines):
        spr, grp = ln.split()
        grp = tuple([int(i) for i in grp.split(',')])
        if fivefold:
            spr = '?'.join([spr] * 5)
            grp *= 5
        spr = collapse(spr)
        result += rec(spr, grp, mem)
    return result


def collapse(line):
    optim = []
    for c in line:
        if c == '.' and optim and optim[-1] == '.':
            continue
        optim.append(c)
    return ''.join(optim)


if __name__ == "__main__":
    main()
