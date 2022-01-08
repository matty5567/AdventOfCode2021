

with open(r'day_2\data.txt') as f:
    data = [(i.split(" ")) for i in f.readlines()]

    ver = sum([int(i[1]) for i in data if i[0] == "down"]) - sum([int(i[1]) for i in data if i[0] == "up"])
    hor = sum([int(i[1]) for i in data if i[0] == "forward"])



print(ver*hor)
