def read_puzzle(file):
    with open(file) as f:
        return [line for line in f.read().split(",")]


def main():
    puzzle = read_puzzle("day2.txt")
    
    part1 = 0
    part2 = 0
    
    for line in puzzle:
        start, end = [int(a) for a in line.split("-")]

        for number in range(start, end+1):
            number_as_string = str(number)
            length_of_number = len(number_as_string)
            length_of_number_div_by_2 = length_of_number // 2

            if length_of_number % 2 == 0:
                number1 = number_as_string[0:length_of_number_div_by_2]
                number2 = number_as_string[length_of_number_div_by_2:]
                part1 += int(number) if number1 == number2 else 0
                
            for l in range(1, length_of_number_div_by_2 + 1):
                if number_as_string == number_as_string[:l] * (len(number_as_string) // l):
                    part2 += number
                    break
                
    print((part1, part2))

if __name__ == '__main__':
    main()