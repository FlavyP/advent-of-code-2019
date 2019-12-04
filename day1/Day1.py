def part1():
    result = 0
    with open('day1.txt', 'r') as file:
        for line in file:
            fuel = int(line) // 3 - 2
            result += fuel
    print(result)


def part2():
    result = 0
    with open('day1.txt', 'r') as file:
        for line in file:
            fuel = int(line)
            while fuel > 0:
                fuel = fuel // 3 - 2
                if fuel > 0:
                    result += fuel
    print(result)


part1()
part2()
