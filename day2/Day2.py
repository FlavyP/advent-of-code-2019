def part1():
    fields = list(eval(open('day2.txt').read()))
    step = 0
    while fields[step] != 99:
        first_pos, second_pos, result_pos = fields[step + 1: step + 4]
        if fields[step] == 1:
            fields[result_pos] = fields[first_pos] + fields[second_pos]
        elif fields[step] == 2:
            fields[result_pos] = fields[first_pos] * fields[second_pos]
        step += 4
    print(fields)


part1()
