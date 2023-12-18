from collections import defaultdict
from queue import PriorityQueue
import math
import time


def main():
    start = time.time()
    with open("input.txt", 'r') as file:
        lines = [line.strip() for line in file]

    sol = dijkstra(0, 3, lines), dijkstra(4, 10, lines)

    print(f"\nPart 1: {sol[0]}\nPart 2: {sol[1]}")
    print(f"Time:   {(time.time() - start) * 1000:.4f} ms")


def dijkstra(lower, upper, lines):
    grid = {}
    for y, ln in enumerate(lines):
        for x, c in enumerate(ln):
            grid[(x, y)] = int(c)

    finish = (len(lines[0]) - 1, len(lines) - 1)
    dists = defaultdict(lambda: math.inf)
    visited = set()

    pq = PriorityQueue()
    pq.put((0, (0, 0), (1, 0), 0))
    pq.put((0, (0, 0), (0, 1), 0))

    while not pq.empty():
        # d: distance, (x,y): coords, (dx, dy): direction, n: steps in current direction
        # prefixes: c: current, n: new
        cd, (cx, cy), (cdx, cdy), cn = pq.get()
        visited.add(((cx, cy), (cdx, cdy), cn))

        if (cx, cy) == finish and cn >= lower:
            return cd

        for ndx, ndy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            if (-cdx, -cdy) == (ndx, ndy):
                continue  # don't turn around

            if (cn < lower and (cdx, cdy) != (ndx, ndy)) or (cn == upper and (cdx, cdy) == (ndx, ndy)):
                continue  # straight line limits

            nx, ny = cx + ndx, cy + ndy
            if (nx, ny) not in grid:
                continue  # out of bounds

            nn = 1 if (cdx, cdy) != (ndx, ndy) else cn + 1
            if ((nx, ny), (ndx, ndy), nn) in visited:
                continue

            nd = cd + grid[(nx, ny)]
            if nd < dists[((nx, ny), (ndx, ndy), nn)]:
                dists[((nx, ny), (ndx, ndy), nn)] = nd
                pq.put((nd, (nx, ny), (ndx, ndy), nn))

    return math.inf


if __name__ == "__main__":
    main()
