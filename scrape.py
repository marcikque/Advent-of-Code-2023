import requests, sys

SESSION = "53616c7465645f5fcc437cbeabfc6511f7358fe605d8372d150859dc73c75892d78a124dc3c6c5c382d6f5a1e70ed1b4164ef170df7fc130a4d2400a6d2ed12e"
HEADERS = {"User-Agent": "Fetch tool"}

def fetch(day: int):
    desc = requests.get(
        f"https://adventofcode.com/2023/day/{day}",
        cookies={"session": SESSION},
        headers=HEADERS)
    inp = requests.get(
        f"https://adventofcode.com/2023/day/{day}/input",
        cookies={"session": SESSION},
        headers=HEADERS)
    try:
        with open(f"Day{str(day).zfill(2)}/input.txt", "w") as f:
            f.write(inp.text)
    except FileNotFoundError:
        print("FNF")
    try:
        with open(f"Day{str(day).zfill(2)}/README.md", "w") as g:
            g.write(desc.text[desc.text.index("<main>"):(desc.text.index("</main>")+8)])
    except FileNotFoundError:
        print("FNF")

if __name__ == "__main__":
    args = sys.argv
    fetch(args[1])
