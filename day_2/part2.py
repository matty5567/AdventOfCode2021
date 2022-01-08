with open(r'day_2\data.txt') as f:
    data = [(i.split(" ")) for i in f.readlines()]

    aim = 0
    hor = 0
    depth = 0

    for i in data:
        val = int(i[1])
        direct = i[0]

        if direct == "down":
            aim += val

        elif direct == "up":
            aim -= val

        elif direct == "forward":
            depth += val * aim
            hor += val



print(depth*hor)
