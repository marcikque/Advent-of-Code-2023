import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = solve(lines, False), solve(lines, True)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def solve(lines, joker_en):
    types = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    cards = {}
    for ln in lines:
        card, bid = ln.split()
        cards[card] = int(bid)
        chars, t = {}, 0
        for c in card:
            chars[c] = chars.get(c, 0) + 1

        if 'J' in chars.keys() and len(chars.keys()) > 1 and joker_en:
            joker = chars.pop('J')
            max_key = max(chars, key=chars.get)
            chars[max_key] += joker

        match tuple(sorted(chars.values())):
            case (5, ):
                t = 7
            case (1, 4):
                t = 6
            case (2, 3):
                t = 5
            case (1, 1, 3):
                t = 4
            case (1, 2, 2):
                t = 3
            case (1, 1, 1, 2):
                t = 2
            case (1, 1, 1, 1, 1):
                t = 1

        types[t].append(card)

    ranking = []
    order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    j_place = 13 if joker_en else 3
    order.insert(j_place, 'J')
    for el in types.values():
        sort = sorted(el, key=lambda s: [order.index(x) for x in s])
        sort.reverse()
        ranking.extend(sort)

    result = 0
    for i, el in enumerate(ranking):
        result += (i + 1) * cards[el]
    return result


if __name__ == "__main__":
    main()
