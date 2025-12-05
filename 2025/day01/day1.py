def read_puzzle(file):
    input = []
    with open(file) as f:
        for line in f.read().split("\n"):
            input.append(line)
        return input


def main():
    puzzle = read_puzzle("day1.txt")

    part1 = 0

    print(part1)

if __name__ == '__main__':
    main()