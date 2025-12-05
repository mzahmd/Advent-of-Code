def read_puzzle(file):
    input = []
    with open(file) as f:
        for line in f.read().split("\n"):
            input.append(line)
        return input


def main():
    puzzle = read_puzzle("day1.txt")
    # puzzle = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

    part1 = 0
    part2 = 0

    position = 50

    for dial in puzzle:
        direction, steps = dial[0], int(dial[1:])
        
        for _ in range(steps):
            if(direction == "L"):
                position -= 1
            else:
                position += 1
                
            if position % 100 == 0:
                part2 += 1
                position = 0
            
        if position == 0:
            part1 += 1

    print((part1, part2))

if __name__ == '__main__':
    main()