import requests, sys

SESSION = "_"
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
