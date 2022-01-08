from itertools import chain

with open(r'day_8\data.txt') as f:
    x = [i.split("|") for i in f.readlines()]
    inputs = [i[0].strip().split(" ") for i in x]
    readings = [i[1].strip().split(" ") for i in x]
    print(len(list(filter(lambda x:len(x) in [2, 3, 4, 7], chain(*readings)))))