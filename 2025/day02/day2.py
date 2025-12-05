def read_puzzle(file):
    input = []
    with open(file) as f:
        for line in f.read().split(","):
            input.append(line)
        return input


def main():
    puzzle = read_puzzle("day2.txt")
    print(puzzle)

if __name__ == '__main__':
    main()