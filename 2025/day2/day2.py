def read_puzzle(file):
    input = []
    with open(file) as f:
        for line in f.read().split("\n"):
            input.append(line)
        return input


def main():
    puzzle = read_puzzle("day2.txt")
    # puzzle = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

if __name__ == '__main__':
    main()